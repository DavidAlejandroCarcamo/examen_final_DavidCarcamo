{
    "name": "Prestamos de Equipos UNICAH - Ejercicio 6",
    "version": "1.0",
    "summary": "Control de prestamos de equipos universitarios",
    "description": "Modulo para administrar prestamos de equipos en UNICAH",
    "author": "David Carcamo",
    "category": "Services",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.access.csv",
        "views/prestamo_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
