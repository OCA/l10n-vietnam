# © 2018 Komit <http://komit-consulting.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class CurrencyRateUpdateService(models.Model):
    _inherit = "currency.rate.update.service"

    @api.multi
    def write(self, vals):
        res = super(CurrencyRateUpdateService, self).write(vals)
        self.force_inverted_currency(self.service, vals)
        return res

    @api.model
    def create(self, vals):
        self.force_inverted_currency(vals.get('service'), vals)
        return super(CurrencyRateUpdateService, self).create(vals)

    def force_inverted_currency(self, service, vals):
        if service == 'VN_VCB' and 'currency_to_update' in vals:
            currencies = self.env['res.currency'].browse(
                vals.get('currency_to_update')[0][2])
            currencies.filtered(
                lambda c: c.name != 'VND' or c.rate_inverted is False).write(
                {'rate_inverted': True}
            )
