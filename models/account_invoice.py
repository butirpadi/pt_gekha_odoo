from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    prepared_by_id = fields.Many2one('hr.employee', 'Prepared by')
    verified_by_id = fields.Many2one('hr.employee', 'Verified by')
    validated_by_id = fields.Many2one('hr.employee', 'Validated by')
    approved_by_id = fields.Many2one('hr.employee', 'Approved by')
    show_signature = fields.Boolean('Show signature', default=False)