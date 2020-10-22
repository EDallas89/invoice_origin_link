# -*- coding: utf-8 -*-
{
    'name': "Invoice Origin Link",

    'summary': """
        Add a link to invoice source document on invoice form view""",
    'author': "Aresoltec Canarias S.L.",
    'website': "https://github.com/EDallas89",
    'category': 'Account',
    'version': '11.0',
    'depends': ['sale', 'account', 'web'],
    'data': [
        'views/account_invoice.xml',
        'templates/assets.xml',
    ],
}