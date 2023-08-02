from flask import Flask,make_response,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    response = make_response("Hello World",200)
    return response

@app.route("/calculator/add", methods=['POST'])
def add():
    number = request.get_json()
    num1 = number['first']
    num2 = number['second']
    result = num1 + num2
    response = make_response({"result":result},200)
    return response

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    number = request.get_json()
    num1 = number['first']
    num2 = number['second']
    result = num1 - num2
    response = make_response({"result":result},200)
    return response

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
