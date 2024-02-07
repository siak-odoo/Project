#-- coding: utf-8 --
from odoo import fields, models

   

class Saving(models.Model):
    _name = 'budget_management.saving'
    _description = 'Saving'

    name = fields.Char(string='Saving Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    budget_id = fields.Many2one('budget.user', string='Budget')

