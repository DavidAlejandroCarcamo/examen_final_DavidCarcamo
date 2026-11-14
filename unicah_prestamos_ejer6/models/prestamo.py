from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PrestamoEquipo(models.Model):
    _name = "unicah.prestamo"
    _description = "Prestamo de equipos UNICAH"

    name = fields.Char(
        string="Codigo de prestamo",
        required=True
    )

    solicitante_id = fields.Many2one(
        "res.partner",
        string="Solicitante",
        required=True
    )

    equipo = fields.Char(
        string="Equipo",
        required=True
    )

    fecha_prestamo = fields.Date(
        string="Fecha de prestamo",
        required=True,
        default=fields.Date.context_today
    )

    fecha_devolucion = fields.Date(
        string="Fecha de devolucion",
        required=True
    )

    estado = fields.Selection([
        ("solicitado", "Solicitado"),
        ("prestado", "Prestado"),
        ("devuelto", "Devuelto"),
    ], string="Estado", default="solicitado", required=True)

    dias_prestamo = fields.Integer(
        string="Dias de prestamo",
        compute="_compute_dias_prestamo",
        store=True
    )

    @api.depends("fecha_prestamo", "fecha_devolucion")
    def _compute_dias_prestamo(self):
        for prestamo in self:
            if prestamo.fecha_prestamo and prestamo.fecha_devolucion:
                prestamo.dias_prestamo = (
                    prestamo.fecha_devolucion
                    - prestamo.fecha_prestamo
                ).days
            else:
                prestamo.dias_prestamo = 0

    @api.constrains("fecha_prestamo", "fecha_devolucion")
    def _check_fechas(self):
        for prestamo in self:
            if (
                prestamo.fecha_prestamo
                and prestamo.fecha_devolucion
                and prestamo.fecha_devolucion < prestamo.fecha_prestamo
            ):
                raise ValidationError(
                    "La fecha de devolucion no puede "
                    "ser anterior a la fecha de prestamo."
                )
