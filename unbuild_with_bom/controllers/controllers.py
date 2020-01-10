# -*- coding: utf-8 -*-
from odoo import http

# class UnbuildWithBom(http.Controller):
#     @http.route('/unbuild_with_bom/unbuild_with_bom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unbuild_with_bom/unbuild_with_bom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unbuild_with_bom.listing', {
#             'root': '/unbuild_with_bom/unbuild_with_bom',
#             'objects': http.request.env['unbuild_with_bom.unbuild_with_bom'].search([]),
#         })

#     @http.route('/unbuild_with_bom/unbuild_with_bom/objects/<model("unbuild_with_bom.unbuild_with_bom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unbuild_with_bom.object', {
#             'object': obj
#         })