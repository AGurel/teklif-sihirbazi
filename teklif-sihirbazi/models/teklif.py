from odoo import fields, models


class TeklifModel(models.Model):
    _name = "teklif.model"

    id = fields.Integer()
    name = fields.Char('Teklif Adı', required=True, translate=False)
