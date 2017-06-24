# -*- coding: utf-8 -*-
# © 2006-2017 Trobz (http://trobz.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Number',
    'version': '10.0.1.0.0',
    'author': 'Trobz,'
              'Odoo Community Association (OCA)',
    'website': 'http://trobz.com',
    'license': 'AGPL-3',
    'category': 'Accounting & Finance',
    'depends': [
        'account',
        'account_voucher',
        'sale',
        'purchase'
    ],
    'data': [
        'views/account_invoice_view.xml',
        'views/account_voucher_view.xml',
    ],
    'installable': True,
}
