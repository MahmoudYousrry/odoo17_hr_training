from odoo import models, fields, api


class HrTrainingParticipation(models.Model):
    _name = 'hr.training.participation'
    _description = 'Training Participation'

    course_id = fields.Many2one('hr.training.course', string="Training Course", required=True, ondelete="cascade")
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)

    attendance_status = fields.Selection([
        ('registered', 'Registered'),
        ('in_process', 'In Process'),
        ('attended', 'Attended'),
        ('absent', 'Absent')
    ], string="Attendance Status", default='registered', required=True)

    department_id = fields.Many2one(
        'hr.department',
        string="Department",
        compute="_compute_department",
        store=True,
    )

    @api.depends('employee_id')
    def _compute_department(self):
        for rec in self:
            rec.department_id = rec.employee_id.department_id



