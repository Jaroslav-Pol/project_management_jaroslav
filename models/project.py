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

    client_id = fields.Many2one('res.partner', string='Client')
    leader_id = fields.Many2one('hr.employee', string='Team lead', domain=[('leader', '=', True)]) #galima pasirinkti tik zmones kurie yra vadovai
    employee_ids = fields.Many2many('hr.employee', string='Employees')

    max_employees = fields.Integer(string='Max team')
    emp_percent = fields.Float(string='Employee percent', compute='_employee_percent')

    @api.depends('max_employees', 'employee_ids')
    def _employee_percent(self):
        for record in self:
            if not record.max_employees:
                record.emp_percent = 0.0
            else:
                record.emp_percent = 100.0 * len(record.employee_ids) / record.max_employees


