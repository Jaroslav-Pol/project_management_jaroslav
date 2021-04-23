from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    project_ids = fields.One2many('project_mngm_jp.project', 'client_id',
                                  string='Projects', readonly=True)


