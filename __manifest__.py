{
    'name': 'Capstone_Simple Change Request',
    'version': '18.0.1.0.0',
    'summary': 'Simple Change Request Management System',
    'description': '''
        Simple Change Request Management System with Word Export
        
        Features:
        * Complete workflow: Draft → Submitted → Approved → Completed
        * Priority levels and request types
        * Effort breakdown management
        * Word document export with mail merge
        * Kanban, List, and Form views
        
        Fully compatible with Odoo 18.0+
    ''',
    'author': 'Your Organization',
    'website': 'https://www.yourwebsite.com',
    'category': 'Project Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/simple_change_request_views.xml',
        'views/change_request_effort_line_views.xml',
        'views/change_request_export_wizard_views.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': ['python-docx', 'docxtpl'],
    },
    # 'post_init_hook': 'post_init_hook',
}
