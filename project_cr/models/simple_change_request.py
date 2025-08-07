from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SimpleChangeRequest(models.Model):
    _name = 'simple.change.request'
    _description = 'Simple Change Request'
    _order = 'create_date desc'
    _rec_name = 'name'
    
    # Basic Information
    name = fields.Char(
        string="Request Title", 
        required=True,
        help="Brief title describing the change request"
    )
    
    description = fields.Text(
        string="Description", 
        required=True,
        help="Detailed description of the change request"
    )
    
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ], string="Priority", default='medium', required=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed')
    ], string="Status", default='draft', required=True)
    
    # User and Department Information
    requester_id = fields.Many2one(
        'res.users', 
        string="Requester", 
        default=lambda self: self.env.user, 
        required=True
    )
    
    department = fields.Char(
        string="Department",
        help="Department or team requesting the change"
    )
    
    request_type = fields.Selection([
        ('system', 'System Change'),
        ('process', 'Process Change'),
        ('policy', 'Policy Change'),
        ('other', 'Other')
    ], string="Request Type", required=True)
    
    # Additional Details
    justification = fields.Text(
        string="Business Justification",
        help="Explain why this change is needed"
    )
    
    impact_analysis = fields.Text(
        string="Impact Analysis",
        help="Analyze the potential impact of this change"
    )
    
    expected_completion = fields.Date(
        string="Expected Completion Date",
        help="When do you expect this change to be completed?"
    )
    
    # System Fields
    create_date = fields.Datetime(string="Created On", readonly=True)
    write_date = fields.Datetime(string="Last Modified", readonly=True)
    
    # Constraints
    @api.constrains('expected_completion')
    def _check_completion_date(self):
        for record in self:
            if record.expected_completion and record.expected_completion < fields.Date.today():
                raise ValidationError("Expected completion date cannot be in the past.")
    
    @api.constrains('name')
    def _check_name_length(self):
        for record in self:
            if record.name and len(record.name) < 5:
                raise ValidationError("Request title must be at least 5 characters long.")
    
    # Model Methods
    @api.model
    def create(self, vals):
        """Override create to generate sequence number"""
        if not vals.get('name') or vals.get('name') == 'New':
            sequence = self.env['ir.sequence'].next_by_code('simple.change.request')
            if sequence:
                vals['name'] = sequence
            else:
                # Fallback sequence generation
                count = self.env['simple.change.request'].search_count([])
                vals['name'] = 'CR-' + str(count + 1).zfill(4)
        return super(SimpleChangeRequest, self).create(vals)
    
    # Action Methods
    def action_submit(self):
        """Submit the change request for approval"""
        for record in self:
            record.state = 'submitted'
        return True
    
    def action_approve(self):
        """Approve the change request"""
        for record in self:
            record.state = 'approved'
        return True
    
    def action_reject(self):
        """Reject the change request"""
        for record in self:
            record.state = 'rejected'
        return True
    
    def action_complete(self):
        """Mark the change request as completed"""
        for record in self:
            record.state = 'completed'
        return True
    
    def action_reset_to_draft(self):
        """Reset the change request to draft state"""
        for record in self:
            record.state = 'draft'
        return True
    
    # Utility Methods
    def name_get(self):
        """Custom name display"""
        result = []
        for record in self:
            name = record.name
            if record.priority == 'urgent':
                name = f"🔴 {name}"
            elif record.priority == 'high':
                name = f"🟡 {name}"
            result.append((record.id, name))
        return result
