# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountVoucher(models.Model):
    _inherit = "account.voucher"

    invoice_number = fields.Integer('Invoice Number')
    invoice_form = fields.Char('Invoice Form', size=10)
    invoice_serie = fields.Char('Invoice Serie', size=10)
