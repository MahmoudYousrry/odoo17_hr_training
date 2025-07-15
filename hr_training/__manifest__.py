{
    "name": "HR Training Management",
    "version": "1.0",
    "depends": ["base", "hr", "hr_contract"],
    "author": "Mahmoud Yousry",
    "category": "Human Resources",
    "description": "Manage internal employee training sessions.",
    "data": [
        "security/ir.model.access.csv",
        'views/actions.xml',
        'views/training_course_views.xml',
        'views/training_participation_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_department_views.xml',
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}