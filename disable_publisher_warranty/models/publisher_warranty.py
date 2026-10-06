# -*- coding: utf-8 -*-
# Parte de disable_publisher_warranty. Licencia LGPL-3.
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class PublisherWarrantyContract(models.AbstractModel):
    """Neutraliza el 'publisher warranty' de Odoo: la comprobación periódica
    que envía a los servidores de Odoo el uuid de la base, el número de
    usuarios, los módulos instalados y la URL pública.

    Pensado SOLO para instancias Community, donde ese envío no cumple ninguna
    obligación de licencia. La instalación se bloquea si hay Odoo Enterprise
    (ver hooks.post_init_hook)."""

    _inherit = "publisher_warranty.contract"

    def update_notification(self, cron_mode=True):
        # No se contacta a Odoo: ni cron ni llamada manual envían nada.
        _logger.info("disable_publisher_warranty: update_notification desactivado")
        return True

    @api.model
    def _get_sys_logs(self):
        # Defensa en profundidad: si algo llama directo a _get_sys_logs, tampoco
        # sale a la red; se devuelve una respuesta vacía con la forma esperada.
        _logger.info("disable_publisher_warranty: _get_sys_logs desactivado")
        return {"messages": [], "enterprise_info": {}}
