from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime as dt

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Data': 'Flavor',"datetime":str(dt.now())}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
