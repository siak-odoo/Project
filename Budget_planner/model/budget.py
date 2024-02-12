#-- coding: utf-8 --
from odoo import fields, models

class Budget(models.Model):

    _name = 'budget.user'
    _description = 'Budget Management'

    name = fields.Char(string='Budget Name', required=True)
    amount = fields.Float(string='Budget Amount', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    state = fields.Selection([
        ('W', 'Week'),
        ('M', 'Month'),
        ('Y', 'Year'),
    ],)
    expense_cost=fields.Float('ExpenseAmount')
    savings_cost=fields.Float('SavingsAmount')
    expenses = fields.One2many('budget_management.expense', 'budget_id', string='Expenses')
    is_recurring = fields.Boolean(string='Recurring Budget')
    budget_category = fields.Selection([
        ('personal', 'Personal'),
        ('business', 'Business'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ], string='Budget Category')
    

