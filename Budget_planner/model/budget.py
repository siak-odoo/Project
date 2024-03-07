#-- coding: utf-8 --
from odoo import fields, models,api

class Budget(models.Model):
    _name = 'budget.user'
    _description = 'Budget Management'

    name = fields.Char(string='Budget Name', required=True)
    amount = fields.Float(string='Budget Amount', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    description = fields.Text("Description")
    state = fields.Selection([
        ('W', 'Week'),
        ('M', 'Month'),
        ('Y', 'Year'),
    ],)
    expense_cost = fields.Float('Expense Amount', compute='_compute_expense_cost', store=True)
    savings_cost = fields.Float('Savings Amount', compute='_compute_savings_cost')
    expenses = fields.One2many('budget.expenseinfo', 'budget_id', string='Expenses')
    is_recurring = fields.Boolean(string='Recurring Budget')
    budget_category = fields.Selection([
        ('personal', 'Personal'),
        ('business', 'Business'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ], string='Budget Category')

    @api.depends('expenses.amount')
    def _compute_expense_cost(self):
        for record in self:
            record.expense_cost = sum(record.expenses.mapped('amount'))

    def _compute_savings_cost(self):
        for record in self:
            record.savings_cost = record.amount - record.expense_cost
    
    
