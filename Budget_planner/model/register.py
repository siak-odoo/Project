#-- coding: utf-8 --
from odoo import fields, models


class Registration(models.Model):
    _name = "register.user"
    _description = "user's authentication"
    Username=fields.Text(required=True)
    Email=fields.Char(required=True)
    Password=fields.Char(required=True)
