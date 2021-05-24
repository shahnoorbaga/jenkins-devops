# -*- coding: utf-8 -*-
from docutils import io

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools.misc import xlwt


class JewelleryManagement(models.Model):
    _name = 'jewellery.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Jewellery Management System'

    jewel_type= [
        ('antique', 'Antique Jewellery'),
        ('temple', 'Temple Jewellery'),
        ('bead', 'Bead Jewellery'),
        ('bridal', 'Bridal Jewellery'),
        ('fashion', 'Fashion Jewellery'),
        ('filigree', 'Filigree Jewellery'),
        ('handmade', 'Handmade Jewellery'),
        ('kundan', 'Kundan Jewellery'),
        ('polki', 'Polki Jewellery'),
        ('minakari', 'Minakari Jewellery'),
        ('navratna', 'Navratna Jewellery'),

    ]
    jewellery_state_id= fields.Many2one('jewellery.state', string="states", default=1)
    name = fields.Char(string="Partner Name")
    street = fields.Char('Street 1')
    street2 = fields.Char('Street 2')
    city = fields.Char('City')
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', string='State')
    payment_term = fields.Text(string="Payment Terms")
    order_date = fields.Date(string="Order date", default=fields.Date.today)
    sale_order_ref = fields.Char(string="Sale Order Reference")
    jewellery_type = fields.Selection(jewel_type, default='antique')
    jewellery_line_ids = fields.One2many('jewellery.line', 'name', string="Jewellery Order Line")
    sale_ids = fields.Many2many('sale.order', string='Transfers')
    sale_count = fields.Integer(string="Sale Count", compute='_compute_sale_ids')
    partner_id = fields.Many2one('res.partner', string="Partner Id")
    # sale_order_ids = fields.Many2many('sale.order', string="Sale Order Id")

    def show_sales(self):
        print('test')

        vals = {
            'name': 'Sale Order jewellery',
            'domain': [('is_jewel', '=', True),('jewel_id','=',self.id)],
            'view_type': 'form',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }
        print(vals)
        return vals

    @api.depends('sale_ids')
    def _compute_sale_ids(self):
        for order in self:
            order.sale_count = len(self.env['sale.order'].search([('jewel_id','=',order.id)]))

    @api.model
    def create(self, vals_list):
        vals_list['name'] = self.env['ir.sequence'].next_by_code('jew_name.id')
        res = super(JewelleryManagement, self).create(vals_list)
        return res

    # To create a sale order for jewellery master
    def create_sale_order_jewel(self):
        order_id = self.env['sale.order'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'date_order': self.order_date,
            'is_jewel': True,
            'jewel_id': self.id,
        })
        print(order_id)
        for line in self.jewellery_line_ids:
            order_line = self.env['sale.order.line'].create({
                'name': _('Sample Order Line'),
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_qty,
                'price_unit': line.unit_price,
                'order_id': order_id.id,
            })
            print(order_line)
        vals = {
            'name': 'Sale Order jewellery',
            'domain': [('is_jewel', '=', True)],
            'view_type': 'form',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }
        return vals

    @api.onchange('partner_id')
    def _change_address(self):
        for rec in self:
            rec.street = rec.partner_id.street
            rec.street2 = rec.partner_id.street2
            rec.city = rec.partner_id.city
            rec.country_id = rec.partner_id.country_id
            rec.state_id = rec.partner_id.state_id

    # def _get_data(self):
    #     current_date = fields.Date.today()
    #     # used to get today’s date#
    #     domain = []
    #     domain += [('date_from', '>=', current_date), (current_date, '<=', self.date_to)]
    #     # used to create a domain to filter based on the start & end date#
    #     res = self.env['model.model'].search(domain)
    #     # created an environment in a variable for the model from which we need to filter the data based on the domain#
    #     docargs = []
    #     docargs.append(
    #         {'key': value}
    #     )
    #
    # def print_report_xls(self):
    #     workbook = xlwt.Workbook()
    #     # Header_style = format_common.font_style(position='center', bold=1, fontos='black',font_height=220, color='grey')
    #     sheet = workbook.add_sheet('Jewellery sale Report')
    #     sheet.row(3).height = 256 * 2
    #     sheet.write_merge(3, 3, 0, 11, u'Jewellery sale Report')
    #     data = self._get_data()
    #     row = 8
    #     for h in data:
    #         sheet.write_merge(row, row, 0, 0, h.get().date_from.strftime('%d/%B/%Y'), values)
    #         sheet.write_merge(row, row, 1, 1, h.get().date_to.strftime('%d/%B/%Y'), values)
    #         row += 1
    #
    #     stream = io.BytesIO()
    #     workbook.save(stream)
    #     Classname('report.module_name.report_name.xlsx', 'model_name')
    #     return self.env.ref('module name.report_action').report_action(self)












