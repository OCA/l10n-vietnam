.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================
Account Invoice Number
======================

## Expected behavior:

# These information should appear on:

- Customer Invoice
- Supplier Invoice
- Sale Receipt (type is Pay Later)
- Purchase Receipt (type is Pay Later)

# Solution:

- Create 3 fields Invoice Number (integer), Form (char, 10 characters), Serie (char, 10 characters) on:

  - Customer 
  - Supplier Invoice
  - Sale Receipt (type is Pay Later)
  - Purchase Receipt (type is Pay Later)

- It is required to have these fields input when:

  - Validating customer/supplier invoice

Usage
=====

To use this module, you need to:

#. Go to ...

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/237/10.0

.. repo_id is available in https://github.com/OCA/maintainer-tools/blob/master/tools/repos_with_ids.txt
.. branch is "8.0" for example


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
