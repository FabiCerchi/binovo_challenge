{
    'name': "Modulo Binovo Challenge",
    'summary': "Website - Blog - Ventas - CRM",
    'version': '16.0.0.0.0',
    'description': '',
    'category': 'website',
    'author': '@FabiCerchi',
    'website': 'https://github.com/FabiCerchi',
    'license': 'LGPL-3',
    'depends': [
        "base",
        "sale",
        "sale_management",
        "crm",
        "website",
        "website_crm",
        "website_blog",
    ],
    "data": [
        'views/blog_inherit_views.xml',
        'views/sale_order_inherit_views.xml',
        'views/crm_lead_inherit_views.xml',
        'security/access_rules.xml',
    ],
    'assets': {
        'website.assets_editor': [
            'binovo_challenge/static/src/js/website_crm_form.js',
        ],
    },
}