from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    age = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)
    rotation = db.Column(db.String(120), nullable=False)  
    diameter = db.Column(db.String(120), nullable=False)   
    favorites = db.relationship('Favorites', backref='planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(120), nullable=False)  
    eye_color = db.Column(db.String(120), nullable=False)   
    favoritos = db.relationship('Favorites', backref='characters', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    manufacturer = db.Column(db.String(120), nullable=False)  
    cost_in_credits = db.Column(db.String(120), nullable=False)   
    favoritos = db.relationship('Favorites', backref='vehicles', lazy=True)

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'),
        nullable=False)
    charancteres_id = db.Column(db.Integer, db.ForeignKey('characters.id'),
        nullable=False)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'),
        nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }