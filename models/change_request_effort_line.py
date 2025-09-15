from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ChangeRequestEffortLine(models.Model):
    _name = 'change.request.effort.line'
    _description = 'Change Request Effort Breakdown Line'
    _order = 'sequence, id'
    
    sequence = fields.Integer(string="Sequence", default=10)
    change_request_id = fields.Many2one(
        'simple.change.request',
        string="Change Request",
        required=True,
        ondelete='cascade'
    )
    
    task_number = fields.Char(
        string="Task No.",
        help="Task number (e.g., 1, 2, 3)"
    )
    
    expected_task = fields.Text(
        string="Expected Task",
        required=True,
        help="Description of the expected task"
    )
    
    effort_days = fields.Float(
        string="Effort (Days)",
        help="Estimated effort in man-days"
    )
    
    remarks = fields.Text(
        string="Remarks",
        help="Additional remarks or notes for this task"
    )
    
    task_category = fields.Selection([
        ('requirements', 'Requirements and Design Specification'),
        ('development', 'Development'),
        ('testing', 'Testing'),
        ('deployment', 'Deployment'),
        ('other', 'Other')
    ], string="Task Category", default='development')
    
    @api.constrains('effort_days')
    def _check_effort_days(self):
        for record in self:
            if record.effort_days < 0:
                raise ValidationError("Effort days cannot be negative.")
