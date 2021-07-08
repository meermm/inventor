from flask import Flask, render_template, request
from flask.wrappers import Response


app = Flask(__name__)

# @app.route('/<test>/')
# def homepage(test):
#     test = test.upper()
#     return render_template('index.html', my_var=test)

@app.route('/')
def homepage():
    f = open('goods.xlsx', 'r', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)



@app.route('/add/', methods=['POST'])
def add():
    good = request.form['good']
    f = open('goods.xlsx', 'a+', encoding='utf-8')
    f.write(good + '\n')
    f.close()
    return """
    <h1>Инвентарь пополнен</h1>
    <a href="/">Домой</a>
    """