# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Project(models.Model):
    _name = 'project_mngm_jp.project'  # pirmas yra modulio(aplanko) pav, kitas modelio
    _description = 'Project management'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    duration = fields.Integer(string='Duration (days)', compute='_project_duration')

    task_ids = fields.One2many('project_mngm_jp.task', 'project_id', string='Tasks')
    invoice_ids = fields.One2many('project_mngm_jp.invoice', 'project_id', string='Invoices')
    client_id = fields.Many2one('res.partner', string='Client')
    leader_id = fields.Many2one('hr.employee', string='Team lead',
                                domain=[('leader', '=', True)])  # galima pasirinkti tik zmones kurie yra vadovai
    employee_ids = fields.Many2many('hr.employee', string='Employees')

    max_employees = fields.Integer(string='Max team', default='1')
    employee_percent = fields.Float(string='Employee percent', compute='_employees_percent')
    employee_amount = fields.Integer(string='Team size', compute='_employee_amount', store=True)
    active = fields.Boolean(default=True, string='Active')



    @api.depends('max_employees', 'employee_ids')
    def _employees_percent(self):
        for record in self:
            if not record.max_employees:
                record.employee_percent = 0.0
            else:
                record.employee_percent = 100.0 * len(record.employee_ids) / record.max_employees


    @api.onchange('max_employees', 'employee_ids')
    def _verify_employees_amount(self):
        if self.max_employees <= 0:
            return {
                'warning': {
                    'title': "Incorrect 'Max team' value",
                    'message': "The number of employees should be positive",
                },
            }
        if self.max_employees < len(self.employee_ids):
            return {
                'warning': {
                    'title': "Too many employees",
                    'message': "Increase team size or remove exces employees",
                },
            }

    @api.constrains('leader_id', 'employee_ids')
    def _verify_leader_not_in_employees(self):
        for record in self:
            if record.leader_id and record.leader_id in record.employee_ids:
                raise exceptions.ValidationError("A project leader can't be an employee in a team")

    @api.depends('start_date', 'end_date')
    def _project_duration(self):
        for record in self:
            if not record.end_date:
                record.duration = 0
                continue
            record.duration = (record.end_date - record.start_date).days

    @api.constrains('employee_ids')
    def _employee_amount(self):
        for record in self:
            record.employee_amount = len(record.employee_ids)


