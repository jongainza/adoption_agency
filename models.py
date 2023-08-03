"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

# from sqlalchemy import text

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = "pets"

    def __repr__(self):
        u = self
        return f"Pet id={u.id} name={u.name} species={u.species} age={u.age} notes={u.notes} available={u.available}"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    species = db.Column(db.String(20), nullable=False)
    photo = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
