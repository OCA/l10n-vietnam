.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================
Account Invoice Number
======================

Vietnamese regulations (from tax authorities) requires to display 3 values on the reports of accounting transactions:

The 3 values to display are:

- Tax Invoice Number
- Tax Invoice Form
- Tax Invoice Series: The references of the series of invoice (the reference of the accounting booklet)

In Odoo, the following types of records need to store those values:

- Customer Invoice
- Supplier Invoice

In Odoo, we need to store this information whenever the issuer of the accounting document is in Vietnam, so this module adds a control when validating a customer/supplier invoice for a issuer based in Vietnam.

Notes:
- Issuer is the Supplier (or Parent Company of the supplier) for Supplier Invoices
- Issuer is Company of the Invoice for Customer Invoices

Usage
=====

To use this module, you need to create / validate any of these:
 - Customer Invoice
 - Supplier Invoice

When validating, a control will ensure that the fields added by this module are being set.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/l10n-vietnam/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Hai Dinh Duong <haidd@trobz.com>
* Vu Nguyen Anh <anhvu@trobz.com>
* Fanha Giang <fanha99@hotmail.com>

Funders
-------

The development of this module has been financially supported by:

* Trobz
* OCV

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
