from odoo import models, fields
class Ticketsk2(models.Model):
	_name = 'ticketsk2'
	_decription ='mis tickets'
	"""docstring for Ticket"""
	
	codigo = fields.Char(string='Código', required=True)
	description = fields.Text(string='Descripción')
	date_start = fields.Date(string='Fecha inicio', default=fields.Date.context_today)
	date_finish = fields.Date(string='Fecha final')

