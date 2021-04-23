from odoo import fields, models


class Employee(models.Model):
    _inherit = 'hr.employee'

    # Add a new column to the hr.employee model, by default partners are not
    # leaders

    leader = fields.Boolean("Team lead", default=False)

    project_ids = fields.Many2many('project_mngm_jp.project',
                                  string='Projects', readonly=True)
