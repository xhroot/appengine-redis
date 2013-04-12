
import webapp2, redis

REDIS_HOST = 'ec2-99-999-999-999.compute-1.amazonaws.com'

class MainHandler(webapp2.RequestHandler):
  def get(self):
    r = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)
    response = ''
    for key in self.request.arguments():
      response += '{0}="{1}"<br>'.format(key, r.get(key))

    self.response.write(response)

  def put(self):
    r = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)
    for key in self.request.arguments():
      r.set(key, self.request.get(key))

  def delete(self):
    r = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)
    for key in self.request.arguments():
      r.delete(key)

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)

