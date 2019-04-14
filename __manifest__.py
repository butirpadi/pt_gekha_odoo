# -*- coding: utf-8 -*-
{
    'name': "TTD on Customer Invoice",

    'summary': """
        Add ttd on customer invoice""",

    'description': """
        Add ttd on customer invoice
    """,

    'author': "butirpadi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'payment_receipt_invoice'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/account_invoice_view.xml',
        'reports/customer_invoice_report.xml',
        'reports/purchase_quotation_report.xml',
        'reports/sale_order_report.xml',
        'reports/payment_receipt_report.xml',
        'views/res_company_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}