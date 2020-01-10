# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MrpUnbuildLine(models.Model):
    _name = 'mrp.unbuild.line'


    product_id = fields.Many2one(comodel_name="product.product", string="Sản phẩm", required=False, )
    bom_product_qty = fields.Float(string="Sản lượng định mức",  required=False, )
    real_product_qty = fields.Float(string="Sản lượng thực tế",  required=False, )
    uom_id = fields.Many2one(comodel_name="uom.uom", string="Đơn vị", required=False, )
    unbuild_id = fields.Many2one(comodel_name="mrp.unbuild", string="Lệnh tháo dỡ", required=False, )
    difference= fields.Float(string="Sai lệch (%)",  required=False, )

    @api.onchange('real_product_qty')
    def onchange_real_product_qty(self):
        if self.onchange_real_product_qty and self.bom_product_qty:
            self.difference = (self.real_product_qty - self.bom_product_qty)* 100 / self.bom_product_qty
