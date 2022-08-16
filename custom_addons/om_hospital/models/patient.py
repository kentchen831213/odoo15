# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    date_of_birth = fields.Date(string='Date of Birth')
    name = fields.Char(string='Name')
    ref = fields.Char(string="Reference")
    age = fields.Integer(string='Age', compute="_compute_age")
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    active = fields.Boolean(string="Active",default="True")

    @api.depends('date_of_birth')
    def _compute_age(self):

        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                print('rec',rec,rec.name,rec.date_of_birth)
                rec.age = today.year-rec.date_of_birth.year
            else:
                rec.age = 0