# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = 'Adding boolean field is jewellery'

    is_jewellery = fields.Boolean(string="Is Jewellery?")
