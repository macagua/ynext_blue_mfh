# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################

from odoo import models, fields

class ProductTemplate(models.Model):
    # python-inherited models
    _inherit = 'product.template'

    family_blue = fields.Char('Family')
