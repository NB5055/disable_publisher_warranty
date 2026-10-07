# disable_publisher_warranty

Módulo Odoo que **neutraliza el "publisher warranty"**: la comprobación
periódica (cron *Publisher: Update Notification*) que envía a los servidores de
Odoo el `database.uuid`, el número de usuarios, los módulos instalados y la URL
pública de la base.

**Solo para instancias Community.** Si la base tiene Odoo Enterprise instalado
(`web_enterprise`), la instalación se cancela a propósito: quitar esa
comprobación en una base Enterprise sería eludir la validación de licencia.

## Qué hace
- Sobrescribe `publisher_warranty.contract.update_notification` y `_get_sys_logs`
  para que no salga ningún dato a la red.
- Al instalar, desactiva el cron del publisher warranty.
- Al desinstalar, lo reactiva (deja la base como estaba).

## Compatibilidad
Una sola rama `main`, API moderna de Odoo: válida de **Odoo 12 a 20**. La serie
9.0 (Python 2) necesitaría una variante aparte.

Licencia: LGPL-3. Autor: NB5055.
