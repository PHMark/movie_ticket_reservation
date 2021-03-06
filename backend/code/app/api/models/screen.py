from datetime import datetime
from typing import List

from db import db
from .cinema import CinemaModel


class ScreenModel(db.Model):
    """A model that will interact with the screen table SQL queries.

    Contains multiple functions that can perform the basic CRUD operation
    for 1 row/entry in the screen table.
    """

    __tablename__ = "screen"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    cinema_id = db.Column(db.Integer, db.ForeignKey("cinema.id"), nullable=False)
    cinema = db.relationship(CinemaModel, backref="cinema", lazy=True)
    seat = db.relationship("SeatModel", backref="screen_seat", lazy=True)

    def __init__(self, name, capacity, cinema):
        self.name = name
        self.capacity = capacity
        self.cinema = cinema

    def json(self):
        """JSON representation of the ScreenModel."""
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity,
            "cinema": self.cinema.json()
        }

    @classmethod
    def find_by_id(cls, id: int) -> "ScreenModel":
        """Find a screen in the database by id."""
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_id_cinema(cls, cinema_id: int, id: int) -> "ScreenModel":
        """Find a screen in the database by id and cinema_id."""
        return cls.query.filter_by(id=id, cinema_id=cinema_id).first()

    @classmethod
    def find_by_name(cls, name: str) -> "ScreenModel":
        """Find a screen in the database by name."""
        return cls.query.filter_by(name=name).first()

    def save_to_db(self, seats: int):
        """Save a new screen in the database."""
        db.session.add(self)
        db.session.add_all(seats)
        db.session.commit()

    def update(self, update_data: dict):
        """Update a screen in the database."""
        (db.session.query(ScreenModel)
                   .filter_by(id=self.id)
                   .update(update_data))
        db.session.commit()

    def remove_from_db(self):
        """Remove a screen from the database."""
        db.session.delete(self)
        db.session.commit()


class ScreenListModel(ScreenModel):
    """An extension of ScreenModel.

    All SQL queries that works with an array of
    ScreenModel is implemented here.
    """

    @classmethod
    def find_screens_by_cinema(cls, cinema_id: int) -> List[ScreenModel]:
        """Find a list of screens that is within a specified cinema."""
        return cls.query.filter_by(cinema_id=cinema_id).all()
