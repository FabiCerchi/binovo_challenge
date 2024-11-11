from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        has_zero_qty = self.has_a_zero_qty()
        if has_zero_qty:
            raise UserError(_('No se puede confirmar una orden de venta con líneas con cantidad 0'))
        return super(SaleOrderInherit, self).action_confirm()


    def has_a_zero_qty(self):
        lines = self.order_line.filtered(lambda line: line.product_uom_qty == 0)
        return len(lines) > 0


    def action_unlink_zero_qty_lines(self):
        lines = self.order_line.filtered(lambda line: line.product_uom_qty == 0)
        lines.unlink()
        return True
