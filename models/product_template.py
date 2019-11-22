# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ProductTemplate(models.Model):
    # python-inherited models
    _inherit = 'product.template'

    family_blue = fields.Char('Family')
