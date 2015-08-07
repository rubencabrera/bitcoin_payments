# -*- coding: utf-8 -*-
from openerp import http

# class BitcoinPayments(http.Controller):
#     @http.route('/bitcoin_payments/bitcoin_payments/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bitcoin_payments/bitcoin_payments/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bitcoin_payments.listing', {
#             'root': '/bitcoin_payments/bitcoin_payments',
#             'objects': http.request.env['bitcoin_payments.bitcoin_payments'].search([]),
#         })

#     @http.route('/bitcoin_payments/bitcoin_payments/objects/<model("bitcoin_payments.bitcoin_payments"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bitcoin_payments.object', {
#             'object': obj
#         })