# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'project_mngm_jp.task'#pirmas yra modulio(aplanko) pav, kitas modelio
    _description = 'Tasks'

    name = fields.Char(string='Tasks', required=True)
    project_id = fields.Many2one('project_mngm_jp.project', string='Project')
