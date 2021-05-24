# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Jewellerystate(models.Model):
    _name = 'jewellery.state'
    _description = 'Jewellery states'

    # training_status = [
    #     ('draft', 'Draft'),
    #     ('progress', 'Progress'),
    #     ('done', 'Done'),
    # ]
    sequence = fields.Integer(string="Sequence")
    name= fields.Char(string='Name')
    # state = fields.Selection(training_status, default='draft')
