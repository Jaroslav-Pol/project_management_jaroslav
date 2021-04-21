# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _name = 'project_mngm_jp.project'#pirmas yra modulio(aplanko) pav, kitas modelio
    _description = 'Project management'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')

    task_ids = fields.One2many('project_mngm_jp.task', 'project_id', string='Tasks')
    invoice_ids = fields.One2many('project_mngm_jp.invoice', 'project_id', string='Invoices')

    client_id = fields.Many2one('res.partner', string='Customer')
    leader_id = fields.Many2one('hr.employee', string='Team leaderf')
    employee_ids = fields.Many2many('hr.employee', string='Employees')
