odoo.define('binovo_challenge.website_crm.form', function (require) {
    'use strict';

    var core = require('web.core');
    var FormEditorRegistry = require('website.form_editor_registry');

    const _lt = core._lt;

    FormEditorRegistry.add('create_lead', {
        formFields: [{
            type: 'char',
            required: true,
            name: 'contact_name',
            fillWith: 'name',
            string: _lt('Your Name'),
        }, {
            type: 'tel',
            hidden: true,  // Oculto
            name: 'phone',
            fillWith: 'phone',
            string: _lt('Phone Number'),
        }, {
            type: 'email',
            required: true,
            fillWith: 'email',
            name: 'email_from',
            string: _lt('Your Email'),
        },{
            type: 'char',
            required: false,  // False
            fillWith: 'commercial_company_name',
            name: 'partner_name',
            string: _lt('Your Company'),
        }, {
            type: 'char',
            modelRequired: true,
            name: 'name',
            string: _lt('Subject'),
        }, {
            type: 'text',
            required: true,
            name: 'description',
            string: _lt('Your Question'),
        },{
            type: 'selection',
            required: true,
            fillWith: 'source',
            name: 'source',
            string: _lt('Source'),
            selection: [
                ['third_parties', _lt('Terceros')],
                ['social_network', _lt('Redes Sociales')],
                ['web_search', _lt('Busqueda Web')]
            ],
        },],
        fields: [{
            name: 'team_id',
            type: 'many2one',
            relation: 'crm.team',
            domain: [['use_opportunities', '=', true]],
            string: _lt('Sales Team'),
            title: _lt('Assign leads/opportunities to a sales team.'),
        }, {
            name: 'user_id',
            type: 'many2one',
            relation: 'res.users',
            domain: [['share', '=', false]],
            string: _lt('Salesperson'),
            title: _lt('Assign leads/opportunities to a salesperson.'),
        }],
    });
});
