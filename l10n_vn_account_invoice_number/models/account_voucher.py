# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountVoucher(models.Model):
    _inherit = "account.voucher"

    invoice_number = fields.Integer()
    invoice_form = fields.Char(size=10)
    invoice_serie = fields.Char(size=10)
