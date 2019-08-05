
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Hello, Daniel</h1>')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h3>This is the about page</h3>')

class newspage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h3>Welcome to the News Page</h3>')


routes = [('/', MainPage),('/news', newspage)]
app = webapp2.WSGIApplication(routes, debug=True)