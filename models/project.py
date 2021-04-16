# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _name = 'project_mngm_jp.project'#pirmas yra modulio(aplanko) pav, kitas modelio
    _description = 'Project management'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')

