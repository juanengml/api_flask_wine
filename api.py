from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime as dt
from flask_restful import reqparse
import joblib

app = Flask(__name__)
api = Api(app)


model = joblib.load("model.pkl")
    
class iris_API(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sepal_length')
        parser.add_argument('sepal_width')
        parser.add_argument('petal_length')
        parser.add_argument('petal_width')
        data = parser.parse_args()
        value = [[data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]]
        res = model.predict(value)  
        #print(value)
        #print(res)   
        if res[0] == 0:
             label = "setosa"
        if res[0] == 1:
             label = "versicolor"
        if res[0] == 2:
             label = "virginica"         
        return {"pred":label}
        # data = {"sepal_length":1.1,"sepal_width": 1.0, "petal_length":4.0,"petal_width":4.1}  

class HelloWorld(Resource):
    def get(self):
        return {'Data': 'Flavor',"datetime":str(dt.now())}

api.add_resource(HelloWorld, '/')
api.add_resource(iris_API, '/api')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
