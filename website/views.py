from flask import Blueprint, render_template, request, flash, Flask, redirect, url_for, jsonify, current_app, Response
from .database import db
from .models import Monsters, Users, Chores, ChoreHistory
from datetime import datetime, timedelta

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    monster = Monsters.query.order_by(Monsters.current_health.desc()).first()
    users = Users.query.all()
    chores = Chores.query.all()
    total_damage_dealt = 0
    for user in users:
        total_damage_dealt += user.damage_dealt

    today = datetime.today().date()
    day_of_week = today.weekday()
    if day_of_week == 6:
        sunday = today
        # clear out chore history
        if ChoreHistory.query.filter(ChoreHistory.completed_on < today).all():
            ChoreHistory.query.filter(ChoreHistory.completed_on < today).delete()
            db.session.commit()
            # get total chore damage from existing chore history and update monster health
            total_chore_damage = 0
            chore_history = ChoreHistory.query.all()
            for chore in chore_history:
                total_chore_damage += chore.chore.attack_power
            monster.current_health = monster.starting_health
            monster.current_health -= total_chore_damage
            db.session.commit()
            # reset user damage dealt and reapply chore damage
            for user in users:
                user.damage_dealt = 0
                for chore in chore_history:
                    if chore.user_id == user.id:
                        user.damage_dealt += chore.chore.attack_power
                        db.session.commit()
        
    else:
        sunday = today - timedelta(days=day_of_week+1)
    
    if day_of_week == 5:
        saturday = today
    else:
        saturday = today + timedelta(days=5-day_of_week)

    return render_template('home.html', **locals())

@views.route('/submit_chores', methods=['POST'])
def submit_chores():
    data = request.form
    user_id = data.get('select_name')
    chore_id = data.get('select_chore')
    chore = Chores.query.filter_by(id=chore_id).first()
    user = Users.query.filter_by(id=user_id).first()

    new_chore_history = ChoreHistory(chore_id=chore_id, user_id=user_id, completed_on=datetime.now())
    db.session.add(new_chore_history)
    db.session.commit()

    chore_damage = chore.attack_power
    if not user.damage_dealt:
        user.damage_dealt = chore_damage
    else:
        user.damage_dealt += chore_damage
    db.session.commit()

    monster = Monsters.query.order_by(Monsters.current_health.desc()).first()
    monster.current_health -= chore_damage
    if monster.current_health <= 0:
        monster.current_health = 0
        most_damage_dealt_by = monster.most_damage_dealt_by
        if most_damage_dealt_by:
            if most_damage_dealt_by != user_id:
                most_damage_user = Users.query.filter_by(id=most_damage_dealt_by).first()
                if most_damage_user.damage_dealt > user.damage_dealt:
                    monster.most_damage_dealt_by = user_id
        else:
            monster.most_damage_dealt_by = user_id
    db.session.commit()
    return redirect(url_for('views.home'))