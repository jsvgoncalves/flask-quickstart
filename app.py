# -*- coding: utf-8 -*-
#
#

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/something')
def register():
    return render_template('index.html')


@app.route('/something-else', methods=['GET', 'POST'])
def login():
    return render_template('index.html')
    # if request.method == 'POST':
    #    # do_something()
    # else:
    #    # do_something_else()

@app.route('/register', methods=['POST'])
def betterRegister():
    user = request.form["rhcloud-login"]
    return render_template('index.html', username=user)


@app.route('/logout', methods=['POST'])
def logout():
    return render_template('index.html')



if __name__ == '__main__':
    app.debug = False  # Use true for local development
    app.run()
