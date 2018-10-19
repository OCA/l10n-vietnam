# © 2018 Komit <http://komit-consulting.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class CurrencyRateUpdateService(models.Model):
    _inherit = "currency.rate.update.service"

    @api.multi
    def write(self, vals):
        self.fore_inverted_currency(self.service, vals)
        return super(CurrencyRateUpdateService, self).write(vals)

    @api.model
    def create(self, vals):
        self.fore_inverted_currency(vals.get('service'), vals)
        return super(CurrencyRateUpdateService, self).create(vals)

    def fore_inverted_currency(self, service, vals):
        if service == 'VN_VCB':
            for currency_id in vals.get('currency_to_update')[0][2]:
                currency = self.env['res.currency'].browse(currency_id)
                if currency.name == 'VND':
                    continue
                currency.write({'rate_inverted': True})
