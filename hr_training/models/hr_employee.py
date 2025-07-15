from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_instructor = fields.Boolean(string="Is Instructor", help="Check if this employee can be assigned as a training instructor")

    training_participation_ids = fields.One2many(
        'hr.training.participation',
        'employee_id',
        string="Training Participations"
    )

    training_participation_count = fields.Integer(
        string="Training Count",
        compute="_compute_training_participation_count"
    )

    @api.depends('training_participation_ids')
    def _compute_training_participation_count(self):
        for employee in self:
            employee.training_participation_count = len(employee.training_participation_ids)

    def action_open_participations(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Participants',
            'res_model': 'hr.training.participation',
            'view_mode': 'tree,form',
            'domain': [('employee_id', '=', self.id)],
            'target': 'current',
        }