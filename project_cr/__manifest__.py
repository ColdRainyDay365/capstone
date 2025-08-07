{
    'name': 'Simple Change Request',
    'version': '18.0.1.0.0',
    'summary': 'Simple Change Request Management System',
    'description': '''
        Simple Change Request Management System
        =====================================
        
        This module provides a comprehensive change request management system with:
        
        Features:
        * Intuitive change request form with comprehensive fields
        * Complete workflow: Draft → Submitted → Approved → Completed
        * Priority levels: Low, Medium, High, Urgent
        * Request types: System, Process, Policy, Other
        * Advanced search and filtering capabilities
        * User-friendly web interface
        * Open access permissions for all users
        * Automatic request numbering (CR-0001, CR-0002, etc.)
        * Demo data included for testing
        * Kanban, List, and Form views
        * Field validation and constraints
        
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
        'python': [],
    },
}
