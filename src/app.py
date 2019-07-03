from flask import Flask, json, Blueprint
from flask_restplus import Api, Namespace, fields, Resource

app = Flask(__name__)

class Config:
  DEBUG = True

app.config.from_object(Config)

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask RESTPlus API',
          version='1.0',
          description='Get start flask',
          # doc=False,
          doc='/'
          )

hello_ns = Namespace('hello', description="Hello flask.")
@hello_ns.route("", "/")
class Healthz(Resource):
  @hello_ns.response(200, 'Hello, I\'m Flask')
  def get(self):
    """Get Hello"""
    return 'Hello, I\'m Flask', 200

api.add_namespace(hello_ns, path="/hello")

app.register_blueprint(blueprint)
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app) # for http or https

app.run(host="0.0.0.0", port="8080")
