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

    expenses = fields.One2many('budget_management.expense', 'budget_id', string='Expenses')
    savings = fields.One2many('budget_management.saving', 'budget_id', string='Savings')

