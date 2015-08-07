# -*- coding: utf-8 -*-
{
    'name': "bitcoin_payments",

    'summary': """
        Accept bitcoin payments.""",

    'description': """
        Add a QR code to the invoice with the bitcoin transaction. 
    """,

    'author': "bisneSmart",
    'website': "http://www.bisnesmart.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'external_dependencies': ['python': 'bitpay-py2']

    # any module necessary for this one to work correctly
    'depends': ['base',
                'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],

}