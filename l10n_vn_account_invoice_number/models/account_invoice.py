# -*- coding: utf-8 -*-
# Copyright 2017 Trobz (http://trobz.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    tax_invoice_number = fields.Integer()
    tax_invoice_form = fields.Char()
    tax_invoice_serie = fields.Char()
    is_owner_in_vietnam = fields.Boolean(string='Is Owner in Vietnam', store=False, compute='_is_owner_in_vietnam')

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        self._is_owner_in_vietnam()
        return super(AccountInvoice, self)._onchange_partner_id()

    @api.one
    def _is_owner_in_vietnam(self):
        invoice_owner_country_code = ''
        if self.type == 'out_invoice' or self.type == 'in_refund':
            invoice_owner_country_code = self.env.user.company_id.partner_id.country_id.code
        else:
            invoice_owner_country_code = self.partner_id.country_id.code
        if invoice_owner_country_code == 'VN':
            self.is_owner_in_vietnam = True
        else:
            self.is_owner_in_vietnam = False

    @api.multi
    def action_invoice_open(self):
        # Check invoice number, form, serie before validating
        if self.is_owner_in_vietnam:
            for inv in self:
                if not inv.tax_invoice_number:
                    raise UserError(
                        _("Missing tax invoice number"))
                if not inv.tax_invoice_form:
                    raise UserError(
                        _("Missing tax invoice form"))
                if not inv.tax_invoice_serie:
                    raise UserError(
                        _("Missing tax invoice serie"))
        return super(AccountInvoice, self).action_invoice_open()
