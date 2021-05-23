from app import db
from datetime import datetime


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now)
    name = db.Column(db.String(140), unique=True)
    quantity = db.Column(db.Integer)
    distance = db.Column(db.Integer)

    def __repr__(self):
        return f'<Table id: {self.id}, name: {self.name}, quantity: {self.quantity}, distance: {self.distance}'

