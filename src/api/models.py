from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import (
    generate_password_hash, check_password_hash
)

db = SQLAlchemy()


user_to_planet = db.Table(
    "user_to_planet",
    db.metadata,
    db.Column("node_id_parent", db.Integer, db.ForeignKey('users.id')),
    db.Column("node_id_child", db.Integer, db.ForeignKey('planets.id')),
)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(255), unique=False, nullable=False)
    is_active = db.Column(
        db.Boolean(),
        unique=False,
        nullable=False,
        default=True
    )

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self._password, password)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(255))
    birth_year = db.Column(db.String(255))
    eye_color = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    hair_color = db.Column(db.String(255))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    skin_color = db.Column(db.String(255))

    def serialize(self):
        return {
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
        }


class Planets(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(255))
    diameter = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    gravity = db.Column(db.Float)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(255))
    terrain = db.Column(db.String(255))
    surface_water = db.Column(db.Float)
    users = db.relationship(
        "Users",
        secondary=user_to_planet,
        primaryjoin=(id == user_to_planet.c.node_id_child),
        secondaryjoin=(id == user_to_planet.c.node_id_parent),
        uselist=True,
        viewonly=True,
        backref="fav_planets"
    )

    def serialize(self):
        return {
            "name": self.name,
            "diameter": self.diameter,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }


lesson_to_lesson = db.Table(
    "lesson_page_to_lesson_page",
    db.metadata,
    db.Column("node_id_parent", db.Integer, db.ForeignKey('lesson_page.id')),
    db.Column("node_id_child", db.Integer, db.ForeignKey('lesson_page.id')),
)


class LessonPage(db.Model):
    __tablename__ = "lesson_page"
    id = db.Column(db.Integer, primary_key=True)
    # Group id for lessons.
    lesson_group = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.Text, nullable=True)
    paragraph = db.Column(db.Text, nullable=True)
    # relationship for the lesson to lesson relationship
    next_lesson = db.relationship(
        "LessonPage",
        secondary=lesson_to_lesson,
        primaryjoin=(id == lesson_to_lesson.c.node_id_parent),
        secondaryjoin=(id == lesson_to_lesson.c.node_id_child),
        backref="prev_lesson",
        single_parent=True,
        uselist=False
    )

