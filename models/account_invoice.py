# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    origin_m2o = fields.Many2one(
        comodel_name='sale.order',
        compute='_compute_origin',
    )

    @api.one
    @api.depends('origin')
    def _compute_origin(self):
        self.origin_m2o = self.env['sale.order'].search([('name', '=', self.origin)], limit=1).id
