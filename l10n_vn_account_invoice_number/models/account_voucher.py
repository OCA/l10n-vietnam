# -*- coding: utf-8 -*-
# Copyright 2017 Trobz (http://trobz.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountVoucher(models.Model):
    _inherit = "account.voucher"

    invoice_number = fields.Integer()
    invoice_form = fields.Char(size=10)
    invoice_serie = fields.Char(size=10)
