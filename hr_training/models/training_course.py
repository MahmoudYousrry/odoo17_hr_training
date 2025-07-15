from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrTrainingCourse(models.Model):
    _name = 'hr.training.course'
    _description = 'Training Course'

    name = fields.Char(string="Course Name", required=True)
    date_start = fields.Date(string="Start Date", required=True)
    sessions_count = fields.Integer(string="Number of Sessions", required=True)
    expected_end_date = fields.Date(string="Expected End Date", compute="_compute_expected_end_date", store=True)
    department_id = fields.Many2one('hr.department', string="Department", required=True)
    instructor_id = fields.Many2one('hr.employee', string="Instructor", domain="[('is_instructor', '=', True)]")
    description = fields.Text(string="Description")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_process', 'In Process'),
        ('done', 'Done'),
    ], string="Status", default='draft', tracking=True)

    participation_ids = fields.One2many(
        'hr.training.participation',
        'course_id',
        string="Participants"
    )

    @api.depends('date_start', 'sessions_count')
    def _compute_expected_end_date(self):
        for rec in self:
            if rec.date_start and rec.sessions_count:
                date = rec.date_start
                sessions_left = rec.sessions_count

                while sessions_left > 0:
                    if date.weekday() not in (4, 5):
                        sessions_left -= 1
                    date += timedelta(days=1)

                rec.expected_end_date = date - timedelta(days=1)
            else:
                rec.expected_end_date = False

    def action_confirm(self):
        for course in self:
            course.state = 'confirmed'

    def action_start_process(self):
        for course in self:
            course.state = 'in_process'
            for participation in course.participation_ids:
                if participation.attendance_status == 'registered':
                    participation.attendance_status = 'in_process'

    def action_done(self):
        for course in self:
            course.state = 'done'
