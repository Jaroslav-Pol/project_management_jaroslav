from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    project_ids = fields.Many2many('project_mngm_jp.project', string='Projects', readonly=True)


