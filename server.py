# -*- coding: utf-8 -*-
import json
import os
from flask import Flask, render_template
from apixu.client import ApixuClient
import utils

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
api_keys = open(os.path.join(SITE_ROOT, 'api_keys.json')).read()
api_keys = json.loads(api_keys)

client = ApixuClient(api_keys.get('apixu_api_key'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calentador/<action>')
def calentador(action):
    if action == 'on':
        data = utils.send_cmd('on')
        return data, 200
    elif action == 'off':
        data = utils.send_cmd('off')
        return data, 200


@app.route("/data")
def render_data():
    filename = os.path.join(app.static_folder, 'data.json')
    with open(filename) as data_json:
        data = json.load(data_json)
    print data
    return json.dumps(data)


@app.route("/weather/<city>")
def weather_data(city):
    current = client.getCurrentWeather(q=city)
    return json.dumps(current)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
