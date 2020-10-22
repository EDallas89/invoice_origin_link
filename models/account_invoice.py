# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    origin_m2m_so = fields.Many2many(
        comodel_name='sale.order',
        compute='_compute_many2many'
    )

    origin_m2m_po = fields.Many2many(
        comodel_name='purchase.order',
        compute='_compute_many2many'
    )

    origin_m2m_ai = fields.Many2many(
        comodel_name='account.invoice',
        compute='_compute_many2many'
    )
    
    @api.depends('origin')
    def _compute_many2many(self):
        if self.origin:
            origin_split = self.origin.split(", ")
            for origin in origin_split:
                self.origin_m2m_so += self.env['sale.order'].search([('name', '=', origin)])
                self.origin_m2m_po += self.env['purchase.order'].search([('name', '=', origin)])
                self.origin_m2m_ai += self.env['account.invoice'].search([('number', '=', origin)])