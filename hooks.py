# -*- coding: utf-8 -*-
# Parte de disable_publisher_warranty. Licencia LGPL-3.
import logging

from odoo import SUPERUSER_ID, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

# Nombre del módulo base de Enterprise: su presencia marca una base Enterprise.
_ENTERPRISE_SENTINEL = "web_enterprise"


def _env(args):
    """Entorno desde los args del hook (17+: (env); <=16: (cr, registry))."""
    if len(args) == 1:
        return args[0]
    return api.Environment(args[0], SUPERUSER_ID, {})


def _warranty_crons(env):
    """Crons del 'publisher warranty' (por modelo o por el código que ejecutan),
    incluidos los ya inactivos."""
    crons = env["ir.cron"].with_context(active_test=False).search([])
    out = env["ir.cron"].browse()
    for cron in crons:
        code = cron.code if "code" in cron._fields else ""
        model = cron.model_id.model if "model_id" in cron._fields and cron.model_id else ""
        if (code and "update_notification" in code) or model == "publisher_warranty.contract":
            out |= cron
    return out


def post_init_hook(*args):
    env = _env(args)
    enterprise = env["ir.module.module"].search(
        [("name", "=", _ENTERPRISE_SENTINEL), ("state", "=", "installed")], limit=1
    )
    if enterprise:
        # Quitar la telemetría de una base Enterprise sería eludir la validación
        # de licencia: este módulo NO se instala ahí.
        raise UserError(
            "disable_publisher_warranty es solo para instancias Community. "
            "Esta base tiene Odoo Enterprise instalado (web_enterprise), "
            "asi que la instalacion se cancela."
        )
    for cron in _warranty_crons(env):
        cron.active = False
        _logger.info("disable_publisher_warranty: cron desactivado: %s", cron.name)


def uninstall_hook(*args):
    # Dejar la base como estaba: reactivar el cron del publisher warranty.
    env = _env(args)
    for cron in _warranty_crons(env):
        cron.active = True
        _logger.info("disable_publisher_warranty: cron reactivado: %s", cron.name)
