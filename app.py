from flask import Flask, render_template
import os


class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]

 
app = Flask(__name__)
app.debug = True
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/app-trial')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/list")
def showMachineList():
    return render_template('list.html')


@app.route("/coolstuff")
def showCoolStuff():
    return render_template('coolstuff.html')


if __name__ == '__main__':

    global is_loaded

    is_loaded = False

    os.environ['PORT'] = '5000'
    port = os.environ['PORT']
    app.run(port=int(port), host='0.0.0.0')