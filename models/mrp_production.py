import json
import datetime
import math
import re

from ast import literal_eval
from collections import defaultdict
from dateutil.relativedelta import relativedelta
import logging
from odoo import api, fields, models, _, Command
from odoo.tools.safe_eval import safe_eval
_logger = logging.getLogger(__name__)
class MP(models.Model):
    _inherit = "mrp.production"
    printer_id = fields.Many2one('iot.device',domain="[('type','=','printer')]")
    report_id_to_print = fields.Many2one('ir.actions.report',compute='_compute_report_id_to_print', store=True, readonly=False)

    @api.depends('bom_id')
    def _compute_report_id_to_print(self):
        for mp in self:
            if not mp.report_id_to_print and  mp.bom_id.report_id_to_print:
                mp.report_id_to_print = mp.bom_id.report_id_to_print