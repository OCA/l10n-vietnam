# © 2018 Komit <http://komit-consulting.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestCurrencyRateUpdateVnVcb(common.SavepointCase):

    def setUp(self):
        super(TestCurrencyRateUpdateVnVcb, self).setUp()
        self.usd = self.env.ref('base.USD')
        self.euro = self.env.ref('base.EUR')
        self.vnd = self.env.ref('base.VND')
        self.vnd.write({'active': True})
        currency_rates = self.env['res.currency.rate'].search(
            [('currency_id', '=', self.usd.id)])
        currency_rates.unlink()
        currency_rates = self.env['res.currency.rate'].search(
            [('currency_id', '=', self.euro.id)])
        currency_rates.unlink()
        currency_rates = self.env['res.currency.rate'].search(
            [('currency_id', '=', self.vnd.id)])
        currency_rates.unlink()
        self.main_currency = self.env.user.company_id.currency_id
        self.update_service = self.env['currency.rate.update.service'].create({
            'service': 'VN_VCB',
            'currency_to_update': [(6, 0,
                                    [self.euro.id, self.vnd.id, self.usd.id])]
        })

    def test_currency_rate_update_USD_VND(self):
        curr = self.vnd
        if self.main_currency.name == 'VND':
            curr = self.usd
        self.update_service.refresh_currency()
        currency_rates = self.env['res.currency.rate'].search(
            [('currency_id', '=', curr.id)])
        self.assertTrue(currency_rates)

    def test_currency_rate_update_VND_EUR(self):
        curr = self.euro
        if self.main_currency.name == 'EUR':
            curr = self.vnd
        self.update_service.refresh_currency()
        currency_rates = self.env['res.currency.rate'].search(
            [('currency_id', '=', curr.id)])
        self.assertTrue(currency_rates)
