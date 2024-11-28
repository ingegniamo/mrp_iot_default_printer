
from odoo import api, fields, models, _
class MP(models.Model):
    _inherit = "mrp.bom"
    report_id_to_print = fields.Many2one('ir.actions.report')