from website.database import db
from sqlalchemy import ForeignKey

__all__ = ['Monsters', 'Users', 'Chores', 'ChoreHistory']

class Monsters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    starting_health = db.Column(db.Integer)
    current_health = db.Column(db.Integer)
    most_damage_dealt_by = db.Column(db.Integer, ForeignKey('users.id'))

    user_dealt_most_damage = db.relationship('Users', backref='monsters')

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    damage_dealt = db.Column(db.Integer)

class Chores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    attack_power = db.Column(db.Integer)
    roll_20_value = db.Column(db.Integer)

class ChoreHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chore_id = db.Column(db.Integer, ForeignKey('chores.id'))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    completed_on = db.Column(db.DateTime)
    
    chore = db.relationship('Chores', backref='chore_history')
    user = db.relationship('Users', backref='chore_history')