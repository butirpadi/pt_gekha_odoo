from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class Company(models.Model):
    _inherit = "res.company"

    signature_on_cust_invoice = fields.Boolean('Signature on Customer Invoice', default=False)
    signature_on_purchase_order = fields.Boolean('Signature on Customer Invoice', default=False)
    signature_on_sale_order = fields.Boolean('Signature on Customer Invoice', default=False)
    signature_on_payment_receipt = fields.Boolean('Signature on Payment Receipt', default=False)
    prepared_by_id = fields.Many2one('hr.employee', 'Prepared by')
    verified_by_id = fields.Many2one('hr.employee', 'Verified by')
    validated_by_id = fields.Many2one('hr.employee', 'Validated by')
    approved_by_id = fields.Many2one('hr.employee', 'Approved by')