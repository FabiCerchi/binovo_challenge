from odoo import models, fields, api, _


class BlogBlogInherit(models.Model):
    _inherit = 'blog.blog'

    company_id = fields.Many2one('res.company', string='Company')

class BlogPostInherit(models.Model):
    _inherit = 'blog.post'

    company_id = fields.Many2one(related='blog_id.company_id', string='Company')