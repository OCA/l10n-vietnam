# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    invoice_number = fields.Integer()
    invoice_form = fields.Char(size=10)
    invoice_serie = fields.Char(size=10)

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
