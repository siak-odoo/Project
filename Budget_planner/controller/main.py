# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class BudgetWebsite(http.Controller):

    @http.route('/budgets', auth="public", website=True)
    def budgetplanner(self,listed_after=None,page=1,**kw):
        # Set the number of budgets per page
        page = int(page)
        budgets_per_page = 2
        # Filter budgets based on the listed_after parameter
        domain = [('state', 'in', ['W','M','Y'])]
        if listed_after:
            domain.append(('create_date', '>=', listed_after))
        # Calculate offset based on the current page
        offset = (page - 1) * budgets_per_page
        # Fetch available budgets with a limit and offset
        budgets = request.env['budget.user'].search(domain, limit=budgets_per_page, offset=offset, order='create_date DESC')
        # Get the total number of budgets for pagination
        total_budgets = request.env['budget.user'].search_count(domain)
        # Calculate the total number of pages
        total_pages = int((total_budgets + budgets_per_page - 1) / budgets_per_page)
        return request.render('Budget_planner.budget_grid', {
            'budgets': budgets,
            'page': page,
            'total_pages': total_pages,
            'listed_after': listed_after,
        })

    @http.route('/budgets/<string:name>', auth="public", website=True)
    def budget_details(self, name):
        budget_obj = http.request.env['budget.user'].search([('name', '=', name)])
        return http.request.render('Budget_planner.budget_details', {'budget': budget_obj[0]})
