#-- coding: utf-8 --
from odoo import fields, models

class Budget(models.Model):
    _name = 'budget.user'
    _description = 'Budget Management'

    name = fields.Char(string='Budget Name', required=True)
    amount = fields.Float(string='Budget Amount', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    description=fields.Text("Description")
    state = fields.Selection([
        ('W', 'Week'),
        ('M', 'Month'),
        ('Y', 'Year'),
    ],)
    expense_cost=fields.Float('ExpenseAmount')
    savings_cost = fields.Float('SavingsAmount', compute='_compute_savings_cost')
    expenses = fields.One2many('budget.expenseinfo','budget_id', string='Expenses')
    is_recurring = fields.Boolean(string='Recurring Budget')
    budget_category = fields.Selection([
        ('personal', 'Personal'),
        ('business', 'Business'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ], string='Budget Category')
    
    def _compute_savings_cost(self):
        for record in self:
            record.savings_cost = record.amount - record.expense_cost


    

