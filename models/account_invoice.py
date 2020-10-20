# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    origin_m2o_so = fields.Many2one(
        comodel_name='sale.order',
        compute='_compute_origin',
    )

    origin_m2o_po = fields.Many2one(
        comodel_name='purchase.order',
        compute='_compute_origin',
    )

    origin_m2o_ai = fields.Many2one(
        comodel_name='account.invoice',
        compute='_compute_origin',
    )

    @api.one
    @api.depends('origin')
    def _compute_origin(self):
            self.origin_m2o_so = self.env['sale.order'].search([('name', '=', self.origin)], limit=1).id
            self.origin_m2o_po = self.env['purchase.order'].search([('name', '=', self.origin)], limit=1).id
            self.origin_m2o_ai = self.env['account.invoice'].search([('number', '=', self.origin)], limit=1).id