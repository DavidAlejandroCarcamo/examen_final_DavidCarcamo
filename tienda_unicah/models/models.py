# from odoo import models, fields, api


# class tienda_unicah(models.Model):
#     _name = 'tienda_unicah.tienda_unicah'
#     _description = 'tienda_unicah.tienda_unicah'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

