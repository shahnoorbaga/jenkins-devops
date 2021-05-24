# -*- coding: utf-8 -*-
# from odoo import http


# class JewelleryManagement(http.Controller):
#     @http.route('/jewellery_management/jewellery_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jewellery_management/jewellery_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jewellery_management.listing', {
#             'root': '/jewellery_management/jewellery_management',
#             'objects': http.request.env['jewellery_management.jewellery_management'].search([]),
#         })

#     @http.route('/jewellery_management/jewellery_management/objects/<model("jewellery_management.jewellery_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jewellery_management.object', {
#             'object': obj
#         })
