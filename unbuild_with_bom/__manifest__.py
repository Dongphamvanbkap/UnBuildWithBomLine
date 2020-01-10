# -*- coding: utf-8 -*-
{
    'name': "Unbuild with BOM",

    'summary': """Unbuild with BOM""",

    'description': """
        This app helps to input the real quantity numbers of Unbuild Order compare with BOM
    """,

    'author': "Odoo Friendship",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'MRP',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp', 'stock',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'data/data_settings.xml',
        'data/product_data.xml',
        'data/bom_data.xml',

        'views/mrp_unbuild.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}