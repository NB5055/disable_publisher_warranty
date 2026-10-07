# -*- coding: utf-8 -*-
{
    "name": "Disable Publisher Warranty",
    "summary": "Corta la telemetria del publisher warranty (solo Community)",
    "description": "Neutraliza el envio periodico a los servidores de Odoo "
                   "(database.uuid, usuarios, modulos instalados, URL publica). "
                   "Solo para instancias Community: la instalacion se cancela si "
                   "la base tiene Odoo Enterprise (web_enterprise) instalado. "
                   "Compatible con Odoo 12 a 20 (API moderna).",
    "version": "1.0.0",
    "author": "NB5055",
    "license": "LGPL-3",
    "category": "Technical",
    "depends": ["mail"],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "application": False,
}
