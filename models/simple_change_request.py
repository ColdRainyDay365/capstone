from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SimpleChangeRequest(models.Model):
    _name = 'simple.change.request'
    _description = 'Simple Change Request'
    _order = 'sequence, create_date desc'
    _rec_name = 'name'
    
    sequence = fields.Integer(string="Sequence", default=10)
    
    # Basic Information
    name = fields.Char(
        string="Request Title", 
        required=True,
        help="Brief title describing the change request"
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
    
    expected_completion = fields.Date(
        string="Expected Completion Date",
        help="When do you expect this change to be completed?"
    )
    
    # Change Request Document Fields
    project_name = fields.Char(
        string="Project Name",
        help="Name of the project this change request belongs to"
    )
    
    change_request_date = fields.Date(
        string="Change Request Date",
        default=fields.Date.today,
        help="Date when this change request was created"
    )
    
    change_number = fields.Char(
        string="Change Number",
        help="Unique change request number"
    )
    
    problem_statement = fields.Text(
        string="Problem Statement",
        help="Describe the issue, gap, or opportunity that triggered this request"
    )
    
    change_description = fields.Html(
        string="Change Description",
        help="Describe the change being requested with detailed specifications"
    )
    
    acceptance_criteria = fields.Text(
        string="Acceptance Criteria",
        help="List the acceptance criteria for this change"
    )
    
    reason_for_change = fields.Text(
        string="Reason for Change",
        help="Explain why the change is necessary"
    )
    
    benefits_of_change = fields.Text(
        string="Benefits of Change",
        help="Describe the benefits that will result from this change"
    )
    
    delivery_timeline = fields.Text(
        string="Delivery Timeline",
        help="Provide the delivery timeline for this change"
    )
    
    cost_estimation = fields.Text(
        string="Cost Estimation",
        help="Provide cost estimation for this change"
    )
    
    assumptions = fields.Text(
        string="Assumptions",
        help="List the key assumptions for this change request"
    )
    
    payment_milestones = fields.Text(
        string="Payment Milestones",
        help="Define payment milestones for this change request"
    )
    
    # Effort Breakdown Fields
    effort_breakdown_ids = fields.One2many(
        'change.request.effort.line',
        'change_request_id',
        string="Effort Breakdown"
    )
    
    total_effort_days = fields.Float(
        string="Total Effort (Days)",
        compute='_compute_total_effort',
        store=True,
        help="Total effort in man-days"
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
    
    # Computed Fields
    @api.depends('effort_breakdown_ids.effort_days')
    def _compute_total_effort(self):
        for record in self:
            record.total_effort_days = sum(record.effort_breakdown_ids.mapped('effort_days'))
    
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
        
        # Generate change number if not provided
        if not vals.get('change_number'):
            vals['change_number'] = vals.get('name', 'CR-0001')
        
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
    
    # Export Methods
    def export_to_word(self):
        """Export change request to Word document using mail merge"""
        # This will be implemented with a Word template
        return {
            'type': 'ir.actions.act_window',
            'name': 'Export to Word',
            'res_model': 'change.request.export.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_change_request_id': self.id}
        }
    
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
