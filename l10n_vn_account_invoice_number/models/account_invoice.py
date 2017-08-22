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

    @api.multi
    def action_invoice_open(self):
        # Check invoice number, form, serie before validating
        for inv in self:
            if not inv.invoice_number:
                raise UserError(
                    _("Missing invoice number"))
            if not inv.invoice_form:
                raise UserError(
                    _("Missing invoice form"))
            if not inv.invoice_serie:
                raise UserError(
                    _("Missing invoice serie"))
        return super(AccountInvoice, self).action_invoice_open()
