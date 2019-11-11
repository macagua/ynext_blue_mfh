[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue)](https://www.python.org/downloads/release/python-375/)
[![LGPL-3.0](https://img.shields.io/github/license/macagua/ynext_blue_mfh.svg)](https://github.com/macagua/ynext_blue_mfh/blob/master/LICENSE)
[![Tech Doc](http://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.youtube.com/watch?v=npjC2r2iCqg)
[![Help](http://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)

# Blue MFH

Blue MFH, is a Odoo 13 module that let you add customizations for the 'stock' App:

- Add new field after 'categ_id' field.

- Remove 'description' field.

- Add new attribute to 'list_price' field, mark as required 
  when 'family_blue' field is equal to 'demo'.

# Dependencies

This module requires the following dependencies:

- odoo 13 > https://github.com/odoo/odoo

# Install

Download the source code:

```
$ git clone https://github.com/macagua/ynext_blue_mfh.git
```

Move ``ynext_blue_mfh`` folder into ``extra-addons`` Odoo directory:

```
$ mv ynext_blue_mfh /full/path/to/extra-addons/
```

Restart the Odoo instance server, login and got to **Apps** > **Blue MFH** > **Install**

![Install 'Blue MFH' Module](https://raw.githubusercontent.com/macagua/ynext_blue_mfh/master/static/description/install_module.png "Install 'Blue MFH' Module")

Then go to Main menu at left top corner and click to **Inventory** > **Master Data** > **Products** > **click into any product** and click to **Edit** button for edit it or click to **Create** or create a new product.

![Access 'Manage Products' from Inventory App](https://raw.githubusercontent.com/macagua/ynext_blue_mfh/master/static/description/manage_products.png "Access 'Manage Products' from Inventory App")

References
----------

- [Odoo 13 Enterprise - Programando un módulo simple - Hola Mundo — Youtube](https://www.youtube.com/watch?v=npjC2r2iCqg).
