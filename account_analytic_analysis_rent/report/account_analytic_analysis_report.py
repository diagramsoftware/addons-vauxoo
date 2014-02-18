# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    code by rod@vauxoo.com
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from report import report_sxw
from osv import osv
import pooler
from tools.translate import _
class account_analytic_account_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(account_analytic_account_report, self).__init__(cr, uid, name, context=context)



report_sxw.report_sxw('report.account.analytic.account.report','account.analytic.account','addons/account_analytic_analysis_rent/report/account_analytic_analysis_report.rml',parser=account_analytic_account_report)