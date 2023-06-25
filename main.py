from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = "Super Secret Key"
CORS(app, resources={r"/v1/*": {"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/putatoe"
db = SQLAlchemy(app)

FERNET_KEY = "_2S4Rdhycz25AfVaQHRMiFTrpIdsG66h_2FPyvyLM2k="

from model import *
from controller import *

admin = Admin(app)
admin.add_view(ModelView(Test, db.session))

app.run(debug=False, host='0.0.0.0')