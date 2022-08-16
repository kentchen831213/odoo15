# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    patient_id = fields.Many2one(comodel_name='hospital.patient',string='Patient')
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")

    @api.onchange('patient_id')
    def onchange_patient_id(self):

        self.ref = self.patient_id.ref