# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    jewel_id = fields.Many2one("jewellery.management", string="Jewel_id")
    is_jewel = fields.Boolean(string="Is it Jewellery?")
