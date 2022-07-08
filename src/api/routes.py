"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People
from api.utils import generate_sitemap, APIException

from datetime import datetime

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify(
        data=[
            person.serialize() for person in people
        ],
        req_time=datetime.now()
    ), 200


@api.route('/people/<int:id>', methods=['GET'])
def get_person(id):
    person = People.query.filter_by(id=id).first()
    if person is None:
        return jsonify(msg="Person doesn't exist."), 400
    else:
        return jsonify(
            data=person.serialize()
        ), 200
