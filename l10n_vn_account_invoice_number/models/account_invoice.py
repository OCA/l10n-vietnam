# -*- coding: utf-8 -*-
# Copyright 2017 Trobz (http://trobz.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    tax_invoice_number = fields.Char()
    tax_invoice_form = fields.Char()
    tax_invoice_series = fields.Char()
    is_issuer_in_vn = fields.Boolean(string='Is issuer in Vietnam',
                                     store=False,
                                     compute='_compute_is_issuer_in_vn')

    @api.constrains('tax_invoice_number')
    def _check_tin_format(self):
        for invoice in self:
            if invoice.tax_invoice_number and \
                    not invoice.tax_invoice_number.isdigit():
                raise ValidationError(
                    _("Tax Invoice Number can not have characters"))

    @api.onchange('partner_id', 'company_id')
    def _compute_is_issuer_in_vn(self):
        for rec in self:
            if rec.type == 'out_invoice' or rec.type == 'in_refund':
                issuer_country_id = (
                    rec.company_id.partner_id.parent_id.country_id or
                    rec.company_id.partner_id.country_id)
            else:
                issuer_country_id = (
                    rec.partner_id.country_id or
                    rec.partner_id.parent_id.country_id)
            issuer_country_code = (
                issuer_country_id and
                issuer_country_id.code or "VN")
            rec.is_issuer_in_vn = issuer_country_code == 'VN'

    @api.multi
    def action_invoice_open(self):
        # Check invoice number, form, series before validating
        for inv in self:
            if inv.is_issuer_in_vn:
                if inv.company_id.validate_tax_invoice_number:
                    if not inv.tax_invoice_number:
                        raise UserError(
                            _("Missing tax invoice number"))
                    if not inv.tax_invoice_form:
                        raise UserError(
                            _("Missing tax invoice form"))
                    if not inv.tax_invoice_series:
                        raise UserError(
                            _("Missing tax invoice series"))
                inv._check_unique_issuer_tax_invoice_info()
        return super(AccountInvoice, self).action_invoice_open()

    def _check_unique_issuer_tax_invoice_info(self):
        same_tax_inv_info = False

        if not self.tax_invoice_number and not self.tax_invoice_form and\
                self.tax_invoice_series:
            return True

        invoice_duplicate_domain = [
            ('type', '=', self.type),
            ('state', 'in', ('open', 'paid')),
            ('tax_invoice_number', '=', str(self.tax_invoice_number)),
            ('tax_invoice_form', '=ilike', str(self.tax_invoice_form)),
            ('tax_invoice_series', '=ilike', str(self.tax_invoice_series)),
            ('id', '!=', self.id), ]

        if self.type in ('in_invoice', 'out_refund'):
            invoice_duplicate_domain += [
                ('partner_id', '=', self.partner_id.id)]

        same_tax_inv_info = self.search(invoice_duplicate_domain)

        if same_tax_inv_info:
            raise UserError(
                _(
                    "The invoice/refund with tax invoice info '%s %s %s' "
                    "already exists under the number '%s'. "
                ) % (
                    same_tax_inv_info[0].tax_invoice_form,
                    same_tax_inv_info[0].tax_invoice_series,
                    same_tax_inv_info[0].tax_invoice_number,
                    same_tax_inv_info[0].number or '-'))
