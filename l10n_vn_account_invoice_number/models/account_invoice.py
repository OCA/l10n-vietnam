# -*- coding: utf-8 -*-
# Copyright 2017 Trobz (http://trobz.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    tax_invoice_number = fields.Integer()
    tax_invoice_form = fields.Char()
    tax_invoice_series = fields.Char()
    is_issuer_in_vn = fields.Boolean(string='Is issuer in Vietnam',
                                     store=False,
                                     compute='_compute_is_issuer_in_vn')

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        self._compute_is_issuer_in_vn()
        return super(AccountInvoice, self)._onchange_partner_id()

    @api.multi
    def _compute_is_issuer_in_vn(self):
        issuer_country_code = ''
        if self.type == 'out_invoice' or self.type == 'in_refund':
            issuer_country_code = self.company_id.partner_id.country_id.code
        else:
            issuer_country_code = self.partner_id.country_id.code
        self.is_issuer_in_vn = issuer_country_code == 'VN'

    @api.multi
    def action_invoice_open(self):
        # Check invoice number, form, serie before validating
        if self.is_issuer_in_vn:
            for inv in self:
                if not inv.tax_invoice_number:
                    raise UserError(
                        _("Missing tax invoice number"))
                if not inv.tax_invoice_form:
                    raise UserError(
                        _("Missing tax invoice form"))
                if not inv.tax_invoice_series:
                    raise UserError(
                        _("Missing tax invoice series"))
                self._check_unique_issuer_tax_invoice_info()
        return super(AccountInvoice, self).action_invoice_open()

    def _check_unique_issuer_tax_invoice_info(self):
        same_tax_inv_info = False
        if self.type in ('out_invoice', 'in_refund'):
            same_tax_inv_info = self.search([
                ('type', 'in', ('out_invoice', 'in_refund')),
                ('state', 'in', ('open', 'paid')),
                ('tax_invoice_number', '=', str(self.tax_invoice_number)),
                ('tax_invoice_form', '=ilike', str(self.tax_invoice_form)),
                ('tax_invoice_series', '=ilike', str(self.tax_invoice_series)),
                ('id', '!=', self.id), ])
        else:
            same_tax_inv_info = self.search([
                ('partner_id', '=', self.partner_id.id),
                ('type', 'in', ('in_invoice', 'out_refund')),
                ('state', 'in', ('open', 'paid')),
                ('tax_invoice_number', '=', str(self.tax_invoice_number)),
                ('tax_invoice_form', '=ilike', str(self.tax_invoice_form)),
                ('tax_invoice_series', '=ilike', str(self.tax_invoice_series)),
                ('id', '!=', self.id), ])
        if same_tax_inv_info:
            raise UserError(
                (
                    "The invoice/refund with tax invoice info '%s %s %s' "
                    "already exists under the number '%s'. "
                ) % (
                    same_tax_inv_info[0].tax_invoice_form,
                    same_tax_inv_info[0].tax_invoice_series,
                    same_tax_inv_info[0].tax_invoice_number,
                    same_tax_inv_info[0].number or '-'))
