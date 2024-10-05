from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/about')
def about(): return 'I am about page'

@app.route('/time')
def get_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.errorhandler(404)
def page_not_found(error):
    return 'Page not found', 404

@app.errorhandler(500)
def internal_server_error(error):
    return 'Internal server error', 500

if __name__ == '__main__':
    app.run(debug=True)
