# -*- coding: utf-8 -*-
# Copyright 2017 Trobz (http://trobz.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    validate_tax_invoice_number = fields.Boolean(
        help="Check this box if the company force to input "
             "Tax Invoice information when Validating Invoice",
        default=True)
