from flask import Flask
from q10r import q10r
import argparse

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(q10r)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=5000, type=int)
    opt = parser.parse_args()

    app.run(host='0.0.0.0', port=opt.port)
