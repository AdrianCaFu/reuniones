# -*- coding: utf-8 -*-
{
    'name': "Reuniones",

    'summary': 'Módulo para reuniones',

    'description': "Módulo que permite asignar salas para reuniones",

    'author': "Adrián",
    'website': "https://www.acano.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Planificación',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

