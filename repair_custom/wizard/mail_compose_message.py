# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def action_send_mail(self):
        res = super().action_send_mail()
        if self.env.context.get('default_model', False) and self.env.context.get('default_model') == 'repair.order':
            if self.env.context.get('default_res_id', False):
                order_id = self.env['repair.order'].sudo().search(
                    [('id', '=', self.env.context.get('default_res_id', False))], limit=1)
                order_id.write({'state': 'budget_sent'})
        return res
