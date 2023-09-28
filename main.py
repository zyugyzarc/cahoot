from flask import *

app = Flask(__name__)

answers = "BBBCDABCBABAAAAC"

@app.route('/')
def home():

    if request.args:
        print(dict(request.args))
        if int(request.args['q']) <= len(answers):
            if request.args['ans'] == answers[int(request.args['q'])-1]:
                return "correct", 200
            else:
                return "wrong", 202

    with open('main.html') as f:
        resp = make_response(f.read())

    return resp

app.run('0.0.0.0', 8888)
