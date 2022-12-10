"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Vehicles, Favorites
import json


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():

    planets = Planets.query.all()
    planetsList = list(map(lambda obj: obj.serialize(), planets))
    response_body = {
        "results": planetsList
    }

    return jsonify(response_body), 200


@app.route('/characters', methods=['GET'])
def get_Characters():

    characters = Characters.query.all()
    charactersList = list(map(lambda obj: obj.serialize(), characters))
    response_body = {
        "results": charactersList
    }

    return jsonify(response_body), 200

@app.route('/vehicles', methods=['GET'])
def get_vehicles():

    vehicles = Vehicles.query.all()
    vehiclesList = list(map(lambda obj: obj.serialize(), vehicles))
    response_body = {
        "results": vehiclesList
    }

    return jsonify(response_body), 200

@app.route('/favorites', methods=['GET'])
def get_favorites():

    favorites = Favorites.query.all()
    favoritesList = list(map(lambda obj: obj.serialize(), favorites))
    response_body = {
        "results": favoritesList
    }

    return jsonify(response_body), 200

@app.route('/user', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = User(name=body["name"], age=body["age"], email=body["email"], password=body["password"])
    db.session.add(user)
    db.session.commit()

    response_body = {
        "msg": "User created"
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['POST'])
def create_planet():
    body = json.loads(request.data)
    planets = Planets(name=body["name"], population=body["population"], diameter=body["diameter"], rotation=body["rotation"])
    db.session.add(planets)
    db.session.commit()

    response_body = {
        "msg": "Planet created"
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['POST'])
def create_characters():
    body = json.loads(request.data)
    characters = Characters(name=body["name"], gender=body["gender"], height=body["height"], eye_color=body["eye_color"])
    db.session.add(characters)
    db.session.commit()

    response_body = {
        "msg": "Character created"
    }

    return jsonify(response_body), 200

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    body = json.loads(request.data)
    print(body)
    vehicles = Vehicles(name=body["name"], model=body["model"], manufacturer=body["manufacturer"], cost_in_credits=body["cost_in_credits"])
    db.session.add(vehicles)
    db.session.commit()

    response_body = {
        "msg": "Vehicle created"
    }

    return jsonify(response_body), 200



@app.route('/user/<int:userid>', methods=['DELETE'])
def delete_user(userid):

    user = User.query.filter_by(id=userid).first()
    print(user)
    db.session.delete(user)
    db.session.commit()
    response_body = {
        "results": "OK"
    }

    return jsonify(response_body), 200

@app.route('/planets/<int:planetid>', methods=['DELETE'])
def delete_planet(planetid):

    planets = Planets.query.filter_by(id=planetid).first()
    db.session.delete(planets)
    db.session.commit()
    response_body = {
        "results": "Planet deleted"
    }

    return jsonify(response_body), 200

@app.route('/characters/<int:charactersid>', methods=['DELETE'])
def delete_character(charactersid):

    characters = Characters.query.filter_by(id=charactersid).first()
    db.session.delete(characters)
    db.session.commit()
    response_body = {
        "results": "Character deleted"
    }

    return jsonify(response_body), 200


@app.route('/vehicles/<int:vehicleid>', methods=['DELETE'])
def delete_vehicle(vehicleid):

    vehicles = Vehicles.query.filter_by(id=vehicleid).first()
    print(vehicles)
    db.session.delete(vehicles)
    db.session.commit()
    response_body = {
        "results": "Vehicle deleted"
    }

    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)