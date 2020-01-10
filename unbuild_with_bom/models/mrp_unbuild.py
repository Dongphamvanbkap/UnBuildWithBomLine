# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MrpUnbuild(models.Model):
    _inherit = 'mrp.unbuild'


    unbuild_lines = fields.One2many(comodel_name="mrp.unbuild.line", inverse_name="unbuild_id", string="", required=False, )

    @api.onchange('bom_id', 'product_qty')
    def onchange_bom_and_qty_id(self):
        if self.bom_id and self.product_qty:
            unbuild_lines = [(5, 0, 0)]
            bom_product_qty = self.bom_id.product_qty
            bom_lines = self.bom_id.bom_line_ids
            for line in bom_lines:
                unbuild_lines.append((0, 0, {
                    'product_id': line.product_id.id,
                    'bom_product_qty': (self.product_qty * line.product_qty)/bom_product_qty,
                    'real_product_qty': (self.product_qty * line.product_qty)/bom_product_qty,
                    'uom_id': line.product_uom_id.id,
                }))
            self.unbuild_lines = unbuild_lines

    def _generate_produce_moves(self):
        res = super(MrpUnbuild, self)._generate_produce_moves()
        data = {}

        for line in self.unbuild_lines:
            data.update({line.product_id.id: line.real_product_qty,})

        for stock_move in res:
            stock_move.sudo().write({'product_uom_qty': data.get(stock_move.product_id.id, stock_move.product_uom_qty)})
        return res