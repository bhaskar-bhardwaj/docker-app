from flask import Flask
import json
import requests
import pandas
application = Flask(__name__)

@application.route('/')
def hello_world():
   return "Hello World V2"

@application.post('/test')
def post_method():
    return json.dumps({'status':'ok','results':'no results'})

@application.post('/test/1')
def post_method1():
    return 'hello there'

@application.route('/hello')
def new_page():
    return 'its new page'

@application.get('/v1/products')
def products():
    return json.dumps({'status':'ok','results':'hero products'})

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=80)
