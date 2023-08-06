from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    dic = request.get_json()
    return jsonify({"result": dic['first']+dic['second']})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    sub=data['first'] - data['second']
    response={'result':sub}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
