from model import *
from main import db, api, FERNET_KEY
from flask_restful import Api, Resource
from flask import Flask, jsonify, request, Response
from sqlalchemy import and_

class Test(db.Model):
    __tablename__="test"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    message=db.Column("message", db.String(50), default=None)

def errorMessage(text):
    result={
        "error": text,
        "status": False
    }
    response=jsonify(result)
    response.status_code=200
    return response

class Demo(Resource):
    #get method to return the message "Test" from the database
    def get(self):
        data=request.get_json()
        if "id" in data.keys():
            message=data["id"]
        else:
            return errorMessage("id is required")
        get_message=Test.query.filter((Test.id==data["id"])).first()
        result=[]
        result.append({"message":get_message.message})
        return jsonify(result)
    #post method to enter any message to the database
    def post(self):
        data=request.get_json()
        if "message" in data.keys():
            message=data["message"]
        else:
            return errorMessage("message is required")
        new_message=Test(message=message)
        db.session.add(new_message)
        db.session.commit()
        result={
            "error":"",
            "status":True,
        }
        response=jsonify(result)
        response.status_code=200
        return response

#Class for testing
'''class Hello(Resource):
    def get(self):
        result = {"msg": "how"}
        return jsonify(result)'''   

api.add_resource(Demo, '/v1/api/demo')
#api.add_resource(Hello, '/v1/api/hello')