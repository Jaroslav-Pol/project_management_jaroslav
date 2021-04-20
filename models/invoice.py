# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'project_mngm_jp.invoice'#pirmas yra modulio(aplanko) pav, kitas modelio
    _description = 'Invoices'

    name = fields.Char(string='Invoice', required=True)
    total = fields.Float(string='Total') #cia kaip pvz, kol nera tikru saskaitu

    project_id = fields.Many2one('project_mngm_jp.project', string='Project')
