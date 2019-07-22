from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html', name="Tom")


@app.route('/p1')
def p1():
    scores = [{'subject': 'os', 'name': 'ZhangSan', 'score': 70},
              {'subject': 'db', 'name': 'ZhangSan', 'score': 75},
              {'subject': 'os', 'name': 'LiSi', 'score': 80},
              {'subject': 'db', 'name': 'LiSi', 'score': 65}]
    return render_template('p1.html', scores=scores)


@app.route('/p2')
def p():
    return render_template('p2.html')


@app.route('/p3', methods=['POST', "GET"])
def p3():
    if request.method == 'GET':
    #     subject = request.form['subject']
    #     name = request.form['name']
    #     score = request.form['score']
    # else:
        subject = request.args['subject']
        name = request.args['name']
        score = request.args['score']
    return render_template('p3.html', subject=subject, name=name, score=score)


if __name__ == '__main__':
    app.run(host='192.168.0.0', debug=True, port=8080)
