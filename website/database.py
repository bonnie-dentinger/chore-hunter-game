from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__all__ = ['db', 'initialize_extensions']

db = SQLAlchemy()

def initialize_extensions(app: Flask):
    db.init_app(app)
    from website.models import Monsters, Users, Chores, ChoreHistory
    with app.app_context():
        db.create_all()
        if not Monsters.query.all():
            monster = Monsters(name='Nargacuga', starting_health=150, current_health=150)
            db.session.add(monster)
            db.session.commit()
        if not Users.query.all():
            user1 = Users(name='Bonnie', damage_dealt=0)
            user2 = Users(name='Bill', damage_dealt=0)
            user3 = Users(name='Kaelyn', damage_dealt=0)
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
        if not Chores.query.all():
            chore1 = Chores(name='Dishes', description='Gather dishes from house and wash the dishes, including putting away clean dishes', attack_power=10, roll_20_value=1)
            chore2 = Chores(name='Laundry', description='Wash the laundry, fold, and put away', attack_power=25, roll_20_value=2)
            chore3 = Chores(name='Vacuum', description='Vacuum the house', attack_power=5, roll_20_value=3)
            chore4 = Chores(name='Sweep', description='Sweep the house', attack_power=5, roll_20_value=4)
            chore5 = Chores(name='Mop', description='Mop the house', attack_power=5, roll_20_value=5)
            chore6 = Chores(name='Clean Bathroom', description='Clean the bathrooms (counters, sinks, toilets, bathtubs)', attack_power=15, roll_20_value=6)
            chore7 = Chores(name='Clean Kitchen', description='Clean the kitchen (counters, stove/oven, dish washer)', attack_power=15, roll_20_value=7)
            chore8 = Chores(name="Clean Kaelyn's Bedroom", description='Clean the bedroom (toys and clothes off floor and surfaces and put away nicely)', attack_power=10, roll_20_value=8)
            chore9 = Chores(name='Clean Living Room', description='Clean the living room', attack_power=10, roll_20_value=9)
            chore10 = Chores(name='Clean Dining Room', description='Clean the dining room (clear table and clean it)', attack_power=5, roll_20_value=10)
            chore11 = Chores(name='Clean Office', description='Clean the computer room (desk spaces)', attack_power=5, roll_20_value=11)
            chore12 = Chores(name='Clean Master Bedroom', description='Clean the bedroom (clothes off floor, everything cleaned up on surfaces)', attack_power=10, roll_20_value=12)
            chore13 = Chores(name='Clean Car', description='Clean the car (vacuum and wipe down)', attack_power=5, roll_20_value=13)
            chore14 = Chores(name='Mow lawn', description='Mow the lawn', attack_power=50, roll_20_value=14)
            chore15 = Chores(name='Weed garden', description='Weed the garden', attack_power=25, roll_20_value=15)
            chore16 = Chores(name='Pick up toys', description='Pick up the toys (throughout house)', attack_power=10, roll_20_value=16)
            chore17 = Chores(name='Feed snake', description='Feed the snake', attack_power=5, roll_20_value=17)
            chore18 = Chores(name='Take out trash', description='Take out the trash (throughout house, pick up any trash not already thrown away as well)', attack_power=10, roll_20_value=18)
            chore19 = Chores(name='Dust', description='Dust the house', attack_power=10, roll_20_value=19)
            chore20 = Chores(name='Wash the dog', description='Wash the dog (she needs it!)', attack_power=10, roll_20_value=20)
            db.session.add(chore1)
            db.session.add(chore2)
            db.session.add(chore3)
            db.session.add(chore4)
            db.session.add(chore5)
            db.session.add(chore6)
            db.session.add(chore7)
            db.session.add(chore8)
            db.session.add(chore9)
            db.session.add(chore10)
            db.session.add(chore11)
            db.session.add(chore12)
            db.session.add(chore13)
            db.session.add(chore14)
            db.session.add(chore15)
            db.session.add(chore16)
            db.session.add(chore17)
            db.session.add(chore18)
            db.session.add(chore19)
            db.session.add(chore20)
        db.session.commit()
    return None