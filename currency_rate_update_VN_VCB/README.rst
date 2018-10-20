.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================================================================================
Currency Rate Update Joint Stock Commercial Bank for Foreign Trade of Vietnam - Vietcombank service
===================================================================================================

Download exchange rates automatically from
Joint Stock Commercial Bank for Foreign Trade of Vietnam - Vietcombank (Vietcombank) service

Installation
============

To install this module, you need to:

    * clone the branch 11.0 of the repository https://github.com/OCA/l10n-vietnam
    * add the path to this repository in your configuration (addons-path)
    * update the module list
    * search for "Currency Rate Update - VCB" in your addons
    * install the module

The module depends on currency_rate_update module available on https://github.com/OCA/currency

Usage
=====

This module does not change usage, but only adds an additional source of exchange rates when configuring in:
Accounting > Configuration > Multi-currencies > Rate Auto-download

Usage is the same as the module `Currency Usage <https://github.com/OCA/currency/tree/11.0/currency_rate_update>`_.


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-vietnam/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Vo Hoang Dat <dat.vh@komit-consulting.com>

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
