#-- coding: utf-8 --
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Budget-planner',
    'description': 'It allows users to manage their budget ,savings,expenses as per their requirement',
    'summary': 'Budget and expenses management app',
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'version': '1.0',
    'depends': ['base','website'],
    "data": [
        "security/ir.model.access.csv",
        "report/budget_template.xml",
        "report/report_budget.xml", 
        'data/website_data.xml',
        "views/budget_user_views.xml",
        "views/budget_grid.xml",
        "views/budget_details.xml",  
        "views/budget_expense_views.xml",
        "views/saving_goal_views.xml",
        "views/budget_expenseinfo_views.xml",     
        "views/budget_menus.xml",
     ]

}