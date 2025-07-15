from odoo import models, fields

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    training_courses_count = fields.Integer(
        string="Training Courses Count",
        compute="_compute_training_courses_count"
    )

    training_participation_count = fields.Integer(
        string="Participants Count",
        compute="_compute_participation_count"
    )

    def _compute_training_courses_count(self):
        for dept in self:
            dept.training_courses_count = self.env['hr.training.course'].search_count([
                ('department_id', '=', dept.id)
            ])

    def _compute_participation_count(self):
        for dept in self:
            dept.training_participation_count = self.env['hr.training.participation'].search_count([
                ('course_id.department_id', '=', dept.id)
            ])

    def action_open_training_courses(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Department Trainings',
            'res_model': 'hr.training.course',
            'view_mode': 'tree,form',
            'domain': [('department_id', '=', self.id)],
            'target': 'current',
            'context': dict(self.env.context),
        }
