import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'platform': 'Google App Engine',
            'language': 'Python',
            'framework': 'Jinja2'
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class ResourcesHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('resources')
		
        # template_values = {
        #     'platform': 'Google App Engine',
        #     'language': 'Python',
        #     'framework': 'Jinja2'
        # }

        # template = jinja_environment.get_template('index.html')
        # self.response.out.write(template.render(template_values))



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/resources', ResourcesHandler),
], debug=True)
