# -*- coding: utf-8 -*-
from odoo import tools, http
from odoo.addons.website_crm.controllers.website_form import WebsiteForm
from odoo.http import request


class WebsiteFormInherit(WebsiteForm):
    def insert_record(self, request, model, values, custom, meta=None):       
        if model.model == 'crm.lead':
            source = request.params.get('source', '')
            if source:
                values['source'] = source

        result = super(WebsiteFormInherit, self).insert_record(request, model, values, custom, meta=meta)
        return result