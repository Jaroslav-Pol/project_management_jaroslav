# -*- coding: utf-8 -*-
{
    'name': "Project management JP",

    'summary': """Manage projects""",

    'description': """
        Jaroslav module for managing projects:
            - creating project
            - adding clients, workers, tasks, etc
            - printing all information
    """,

    'author': "Jaroslav Polujanskij",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/project_view.xml',
        'views/task_view.xml',
        'views/invoice_view.xml',
        'views/res_partner_inherited_view.xml',
        'views/hr_employee_inherited_view.xml'

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
