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