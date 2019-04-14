# -*- coding: utf-8 -*-
from odoo import http

# class TtdInvoice(http.Controller):
#     @http.route('/ttd_invoice/ttd_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ttd_invoice/ttd_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ttd_invoice.listing', {
#             'root': '/ttd_invoice/ttd_invoice',
#             'objects': http.request.env['ttd_invoice.ttd_invoice'].search([]),
#         })

#     @http.route('/ttd_invoice/ttd_invoice/objects/<model("ttd_invoice.ttd_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ttd_invoice.object', {
#             'object': obj
#         })