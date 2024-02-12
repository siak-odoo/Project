#-- coding: utf-8 --
from odoo import fields, models

class SavingsGoal(models.Model):
    _name = 'budget_management.savings_goal'
    _description = 'Savings Goal'

    name = fields.Char(string='Goal Name', required=True)
    target_amount = fields.Float(string='Target Amount', required=True)
    current_amount = fields.Float(string='Current Amount')
    deadline = fields.Date(string='Deadline')
    budget_id = fields.Many2one('budget.user', string='Budget')
    



