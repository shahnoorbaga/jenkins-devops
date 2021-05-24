# -*- coding: utf-8 -*-

from odoo import models, fields, api


class JewelleryLine(models.Model):
    _name = 'jewellery.line'
    _description = 'Jewellery Sale Line'

    # def _get_default_currency_id(self):
    #     return self.env.company.currency_id.id

    jewellery_sale_id = fields.Many2one('jewellery.management', string="Jewellery Sale Id")
    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.product', string="Product Id", domain="[('is_jewellery', '=', True)]")
    product_qty = fields.Float(string='Product Quantity')
    uom_jewel = fields.Float(string='Unit of Measure')
    # image = fields.Binary(string='Image')
    unit_price = fields.Monetary(string='Unit Price')
    currency_id = fields.Many2one('res.currency', 'Currency', default=lambda self: self.env.company.currency_id.id)
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], help="Technical field for UX purpose.")
    sequence = fields.Integer(string="Sequence")

    @api.onchange('product_id')
    def _change_desc_unitprice(self):
        for rec in self:
            rec.unit_price = rec.product_id.list_price


