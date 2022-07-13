"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint, Response, send_file, current_app
from api.models import db, Pic
from api.utils import generate_sitemap, APIException
from werkzeug.utils import secure_filename
import json



api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



@api.route('/upload', methods=['POST'])
def upload():
    # print("hola")
    body = json.loads(request.data)
    print("holaa",body)
    foto = body["foto"]
    print("foto", foto)

    pic = Pic(img = foto)

    db.session.add(pic)
    db.session.commit()


    return 'img upload', 200

