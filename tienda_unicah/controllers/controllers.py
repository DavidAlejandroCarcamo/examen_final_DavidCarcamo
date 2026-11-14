# from odoo import http


# class TiendaUnicah(http.Controller):
#     @http.route('/tienda_unicah/tienda_unicah', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tienda_unicah/tienda_unicah/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tienda_unicah.listing', {
#             'root': '/tienda_unicah/tienda_unicah',
#             'objects': http.request.env['tienda_unicah.tienda_unicah'].search([]),
#         })

#     @http.route('/tienda_unicah/tienda_unicah/objects/<model("tienda_unicah.tienda_unicah"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tienda_unicah.object', {
#             'object': obj
#         })

