from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from services import *

app = Flask(__name__)
CORS(app)
api = Api(app)

# Sample endpoints just to demonstrate API endpoint call and db connection.
api.add_resource(Home, '/')
api.add_resource(ContactUs, '/contact-us')


if __name__ == '__main__':
    app.run(port=8001)
