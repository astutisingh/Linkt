# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import urllib
import json
 

def get_link_info(api_key, url):
    encoded_url = urllib.parse.quote(url, safe='')
    api_url = "https://ipqualityscore.com/api/json/url/"
    data = requests.get(api_url + api_key + "/" + encoded_url)
    data = json.dumps(data.json())

    return data


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, template_folder='templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods=['POST'])
@cross_origin()
def main():
    default_value = ''
    data = request.get_json()
    api_key = data.get("api_key")
    url = data.get("url")
    # url = "www.lpu.in" # for example
    data = get_link_info(api_key, url)
    print(data)
    return jsonify(data)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run('0.0.0.0', port=8000)
