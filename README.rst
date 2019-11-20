========
Blue MFH
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |tech-docs| |odoo13-docs| |help|
    * - tests
      - | |python37| |odoo13| |travis| |coverall|
    * - license
      - |github-license|
    * - contribute
      - |github-issues| |github-forks| |github-contributors|
    * - share
      - |share-twitter| |github-stars|

.. |tech-docs| image:: http://img.shields.io/badge/tutorial-docs-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.youtube.com/watch?v=npjC2r2iCqg
    :alt: Documentation Source

.. |odoo13-docs| image:: http://img.shields.io/badge/13.0-docs-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.odoo.com/documentation/13.0/index.html
    :alt: Odoo 13 Documentation

.. |help| image:: http://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.odoo.com/forum/help-1
    :alt: Odoo Help

.. |share-twitter| image:: https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmacagua%2Fcybrosys_school
    :target: https://twitter.com/intent/tweet?text=Download%20and%20use%20%27cybrosys_school%27%20package%20for%20doing%20Python%20trainings%20in%20Venezuela%20%F0%9F%87%BB%F0%9F%87%AA%20https://github.com/macagua/cybrosys_school
    :alt: Share at Twitter

.. |github-contributors| image:: https://img.shields.io/github/contributors/macagua/ynext_blue_mfh.svg
    :target: https://github.com/macagua/ynext_blue_mfh/graphs/contributors
    :alt: Github Contributors

.. |github-license| image:: https://img.shields.io/github/license/macagua/ynext_blue_mfh.svg
    :target: https://github.com/macagua/ynext_blue_mfh/blob/master/LICENSE
    :alt: Github License

.. |github-issues| image:: https://img.shields.io/github/issues/macagua/ynext_blue_mfh
    :target: https://github.com/macagua/ynext_blue_mfh/issues
    :alt: Github Issues

.. |github-forks| image:: https://img.shields.io/github/forks/macagua/ynext_blue_mfh
    :target: https://github.com/macagua/ynext_blue_mfh/network/members
    :alt: Github Forks

.. |github-stars| image:: https://img.shields.io/github/stars/macagua/ynext_blue_mfh
    :target: https://github.com/macagua/ynext_blue_mfh/stargazers
    :alt: Github Favorites

.. |python37| image:: https://img.shields.io/badge/Python-3.7-blue
    :target: https://www.python.org/downloads/release/python-375/
    :alt: Python 3.7.5 version

.. |odoo13| image:: https://img.shields.io/badge/Odoo-13-blue
    :target: https://github.com/odoo/odoo/tree/13.0
    :alt: Odoo 13 version

.. |travis| image:: https://travis-ci.org/macagua/ynext_blue_mfh.svg?branch=master
    :target: https://travis-ci.org/macagua/ynext_blue_mfh
    :alt: Travis-CI Build Status

.. |coverall| image:: https://coveralls.io/repos/github/macagua/ynext_blue_mfh/badge.svg?branch=master
    :target: https://coveralls.io/github/macagua/ynext_blue_mfh?branch=master
    :alt: Coveralls Checkout Status

.. end-badges

About
=====

Blue MFH, is a Odoo 13 module that let you add customizations for the 'stock' App:

- Add new field after 'categ_id' field.

- Remove 'description' field.

- Add new attribute to 'list_price' field, mark as required
  when 'family_blue' field is equal to 'demo'.


Features
========

This Odoo 13 module include the follow technical features included:

- Internationalisation (i18n) support.


Dependencies
============

This module requires the following dependencies:

- odoo 13 > https://github.com/odoo/odoo


Install
=======

Download the source code:

::

    $ git clone https://github.com/macagua/ynext_blue_mfh.git


Move ``ynext_blue_mfh`` folder into ``extra-addons`` Odoo directory:

::

    $ mv ynext_blue_mfh /full/path/to/extra-addons/


Restart the Odoo instance server, login and got to **Apps** > **Blue MFH** > **Install**

.. figure:: https://raw.githubusercontent.com/macagua/ynext_blue_mfh/master/static/description/install_module.png
    :align: center
    :width: 70%
    :alt: Install 'Blue MFH' Module

    Install 'Blue MFH' Module

Then go to Main menu at left top corner and click to **Inventory** > **Master Data** > **Products** > **click into any product** and click to **Edit** button for edit it or click to **Create** or create a new product.

.. figure:: https://raw.githubusercontent.com/macagua/ynext_blue_mfh/master/static/description/manage_products.png
    :align: center
    :width: 70%
    :alt: Access 'Manage Products' from Inventory App

    Access 'Manage Products' from Inventory App


Testing
=======

For run the module tests, with the following command:

::

    $ /full/path/to/odoo-bin --addons-path=/full/path/to/addons,/full/path/to/extra-addons \
      -d t -i ynext_blue_mfh --test-enable --stop-after-init --log-level=test


Contribute
==========

- Issue Tracker: https://github.com/macagua/ynext_blue_mfh/issues

- Source Code: https://github.com/macagua/ynext_blue_mfh


License
=======

- The project is licensed under the AGPL-3.


References
==========

- `Odoo 13 Enterprise - Programando un módulo simple - Hola Mundo — Youtube <https://www.youtube.com/watch?v=npjC2r2iCqg>`_.

- `Automated testing in Odoo <https://www.surekhatech.com/blog/automated-testing-in-odoo>`_.

- `Odoo Experience 2018 - Improve the Quality of Your Modules with Automated Tests <https://www.youtube.com/watch?v=jZddEWFdUcM>`_.
