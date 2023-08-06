from __future__ import division
import requests
from flask import Flask, render_template, url_for, request, redirect, session, flash, g, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    if request.method=='GET':
        return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    if request.method=='POST':
        try:
            data = request.get_json()
            print(data)
            add=int(data['first'])+int(data['second'])
            response={'result':add}
            return jsonify(response), 200
        except:
    # if request.method=='GET':
            return jsonify({'message':'error'}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        print(data)
        sub=int(data['first'])-int(data['second'])
        response={'result':sub}
        return jsonify(response), 200
    except:
# if request.method=='GET':
        return jsonify({'message':'error'}), 400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
