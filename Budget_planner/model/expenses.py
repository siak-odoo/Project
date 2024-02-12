#-- coding: utf-8 --
from odoo import fields, models

class Expense(models.Model):
    _name = 'budget_management.expense'
    _description = 'Expense'

    name = fields.Char(string='Expense Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    budget_id = fields.Many2one('budget.user', string='Budget')
    date = fields.Date(string='Expense Date')
    expense_category = fields.Selection([
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('other', 'Other'),
    ], string='Expense Category')
    description = fields.Text(string='Description')


