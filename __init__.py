from . import models

def post_init_hook(cr, registry):
    """Post-install script to create access rights for new models"""
    from odoo import api, SUPERUSER_ID
    
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # Create access rights for effort line model
    effort_line_model = env['ir.model'].search([('model', '=', 'change.request.effort.line')])
    if effort_line_model:
        env['ir.model.access'].create({
            'name': 'change.request.effort.line.all',
            'model_id': effort_line_model.id,
            'perm_read': True,
            'perm_write': True,
            'perm_create': True,
            'perm_unlink': True,
        })
        
        env['ir.model.access'].create({
            'name': 'change.request.effort.line.user',
            'model_id': effort_line_model.id,
            'group_id': env.ref('base.group_user').id,
            'perm_read': True,
            'perm_write': True,
            'perm_create': True,
            'perm_unlink': True,
        })
    
    # Create access rights for export wizard model
    export_wizard_model = env['ir.model'].search([('model', '=', 'change.request.export.wizard')])
    if export_wizard_model:
        env['ir.model.access'].create({
            'name': 'change.request.export.wizard.all',
            'model_id': export_wizard_model.id,
            'perm_read': True,
            'perm_write': True,
            'perm_create': True,
            'perm_unlink': True,
        })
        
        env['ir.model.access'].create({
            'name': 'change.request.export.wizard.user',
            'model_id': export_wizard_model.id,
            'group_id': env.ref('base.group_user').id,
            'perm_read': True,
            'perm_write': True,
            'perm_create': True,
            'perm_unlink': True,
        })
