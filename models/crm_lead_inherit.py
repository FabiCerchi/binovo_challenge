from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    source = fields.Selection(
        [('third_parties', 'Terceros'),
        ("social_network", "Redes Sociales"),
        ("web_search", "Busqueda Web")], string="Fuente")

