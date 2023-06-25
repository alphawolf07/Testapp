from main import db, api, FERNET_KEY
from flask_restful import Api, Resource
from flask import Flask, jsonify, request, Response
from sqlalchemy import and_

class Test(db.Model):
    __tablename__="test"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    message=db.Column("message", db.String(50), default=None)