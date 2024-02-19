#-- coding: utf-8 --
from odoo import fields, models

class Expense(models.Model):
    _name = 'budget.expenseinfo'
    _description = 'Expenseinfo'
   
    name = fields.Many2one('budget.expense', string='Expensename')
    amount = fields.Float(string='Amount', required=True)
    budget_id = fields.Many2one('budget.user',string='Budget')
    expense_category = fields.Selection([
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('other', 'Other'),
    ], string='Expense Category')

    


