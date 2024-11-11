from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestSaleOrderInherit(TransactionCase):

    def setUp(self):
        super(TestSaleOrderInherit, self).setUp()
        
        self.product = self.env['product.template'].create({
            'name': 'Test Product',
            'type': 'consu',
            'list_price': 100.0,
        })

        self.product_2 = self.env['product.template'].create({
            'name': 'Test Product 2',
            'type': 'consu',
            'list_price': 100.0,
        })

        self.sale_order = self.env['sale.order'].create({
            'partner_id': self.env.ref('base.partner_admin').id,
        })


    def test_action_confirm_with_zero_qty_line(self):

        self.sale_order.order_line.create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 0,
        })

        with self.assertRaises(UserError):  
            self.sale_order.action_confirm()
    

    def test_has_a_zero_qty(self):
        self.sale_order.order_line.create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 0,
        })

        self.assertTrue(self.sale_order.has_a_zero_qty())
    

    def test_action_unlink_zero_qty_lines(self):
        self.sale_order.order_line.create({
            'order_id': self.sale_order.id,
            'product_id': self.product.id,
            'product_uom_qty': 0,
        })

        self.sale_order.order_line.create({
            'order_id': self.sale_order.id,
            'product_id': self.product_2.id,
            'product_uom_qty': 5,
        })

        self.sale_order.action_unlink_zero_qty_lines()

        zero_qty_lines = self.sale_order.order_line.filtered(lambda line: line.product_uom_qty == 0)
        self.assertEqual(len(zero_qty_lines), 0, "Existen lineas con cantidad 0 luego de ejecutar")


        
