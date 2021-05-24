# -*- coding: utf-8 -*-
{
    'name': "Jewellery Management System",

    'summary': """
        Manage your jewellery in this module""",

    'description': """
    1. track sales for jewelleries
    2. view in tree, form and kanban
    3. different stages of lead to sales
    4. add jewellery type from quick wizard on the go
    5. create sale order report for every sales
    6. allow access to only valid users
    """,

    'author': "Bista Solutions, Mohammed Zeeshan Jagirdar",
    'website': "http://www.bistasolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'data/ir_module_category_data.xml',
        'security/jewellery_security.xml',
        'security/ir.model.access.csv',

        'data/ir_sequence_data.xml',

        'views/jewellery_sale_views.xml',
        'views/product_template_extended_views.xml',
        'views/jewellery_state_views.xml',
        # 'views/sale_views.xml'
        'views/menu_item_views.xml',

        'report/jewellery_sale_report.xml',
        'report/jewellery_sale_report_template.xml',


    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
