# -- coding: utf-8 --
from odoo import fields, models, api

class Expense(models.Model):
    _name = 'budget.expenseinfo'
    _description = 'Expenseinfo'

    name = fields.Many2one('budget.expense', string='Expensename', required=True)
    amount = fields.Float(string='Amount', compute='_compute_amount', store=True)
    budget_id = fields.Many2one('budget.user', string='Budget', compute='_compute_budget_id', store=True)
    expense_category = fields.Selection([
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('other', 'Other'),
    ], string='Expense Category', compute='_compute_expense_category', store=True)

    @api.depends('name', 'name.amount', 'name.budget_id', 'name.expense_category')
    def _compute_amount(self):
        for record in self:
            record.amount = record.name.amount if record.name else 0.0

    @api.depends('name', 'name.budget_id')
    def _compute_budget_id(self):
        for record in self:
            record.budget_id = record.name.budget_id if record.name else False

    @api.depends('name', 'name.expense_category')
    def _compute_expense_category(self):
        for record in self:
            record.expense_category = record.name.expense_category if record.name else False
