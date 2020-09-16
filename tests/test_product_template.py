# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo.tests import common

_logger = logging.getLogger(__name__)


class TestProductTemplate(common.TransactionCase):

    def setUp(self):
        super(TestProductTemplate, self).setUp()
        # 'product.template' instance model
        self.product_template = self.env['product.template']

        # # create an 'product_template' record
        # self.product_template1 = self.product_template.create({
        #     'family_blue': 'Laptop Blue',
        # })

    def test_product_templates_install(self):
        # This function test the 'product.template' instances creation functionality

        # check if 'family_blue' is not install at 'ir.model.fields'assertEqual
        self.assertFalse(self.env['ir.model.fields'].search([('model', '=', 'family_blue')]))
        _logger.info("The 'family_blue' is not install at 'ir.model.fields'.")

        # check if 'family_blue' is install at 'ir.model.fields'assertEqual
        # self.assertTrue(self.env['ir.model.fields'].search([('model', '=', 'family_blue')]))
        # _logger.info("The 'family_blue' is install at 'ir.model.fields'.")

        _logger.info("Your 'TestProductTemplate' test was successful!")
