# from odoo import http


# class UnicahPrestamosEjer6(http.Controller):
#     @http.route('/unicah_prestamos_ejer6/unicah_prestamos_ejer6', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unicah_prestamos_ejer6/unicah_prestamos_ejer6/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('unicah_prestamos_ejer6.listing', {
#             'root': '/unicah_prestamos_ejer6/unicah_prestamos_ejer6',
#             'objects': http.request.env['unicah_prestamos_ejer6.unicah_prestamos_ejer6'].search([]),
#         })

#     @http.route('/unicah_prestamos_ejer6/unicah_prestamos_ejer6/objects/<model("unicah_prestamos_ejer6.unicah_prestamos_ejer6"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unicah_prestamos_ejer6.object', {
#             'object': obj
#         })

