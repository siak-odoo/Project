#-- coding: utf-8 --
from odoo import fields, models

class Expense(models.Model):
    _name = 'budget_management.expense'
    _description = 'Expense'

    name = fields.Char(string='Expense Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    budget_id = fields.Many2one('budget.user', string='Budget')
