from os import path

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String)
    time = db.Column(db.Float)


class Visits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.Float)


if not path.isfile('chat.db'):
    db.create_all()


def create_user_info(cur_user):
    users_list = [user.name for user in Users.query.all()]
    users_list.remove(cur_user[0].name)
    user_info = {
        'user_name': cur_user[0].name,
        'user_id': cur_user[0].id,
        'user_list': users_list
    }

    return user_info


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    if request.method == 'POST':
        user_info = request.get_json(force=True)
        email = user_info['email']
        password = user_info['password']
        cur_user = Users.query.filter_by(email=email).all()

        if cur_user:
            if check_password_hash(cur_user[0].password, password):

                return jsonify(create_user_info(cur_user))

            else:

                return jsonify({
                    'access': 'denied'
                })

        return jsonify({
                    'access': 'denied'
                })


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_info = request.get_json(force=True)
        name = user_info['name']
        email = user_info['email']
        psw_hash = generate_password_hash(user_info['password'])
        cur_user = Users.query.filter_by(email=email).all()

        if not cur_user:
            user = Users(name=name, email=email, password=psw_hash)
            db.session.add(user)
            db.session.flush()
            db.session.commit()

        cur_user = Users.query.filter_by(email=email).all()

        return jsonify(create_user_info(cur_user))


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        sent_info = request.get_json(force=True)
        receiver = Users.query.filter_by(name=sent_info['receiver']).all()
        receiver_id = receiver[0].id
        sender_id = sent_info['sender_id']
        msg = sent_info['message']
        time = sent_info['time']

        message = Messages(
            sender_id=sender_id,
            receiver_id=receiver_id,
            message=msg,
            time=time
        )

        db.session.add(message)
        db.session.flush()
        db.session.commit()

    return 'ok'


@app.route('/receive_message', methods=['GET', 'POST'])
def recieve_message():
    if request.method == 'POST':
        receiver_info = request.get_json(force=True)
        sender = Users.query.filter_by(name=receiver_info['sender']).all()
        sender_id = sender[0].id
        receiver_id = receiver_info['receiver_id']
        last_time = receiver_info['last_time']
        receive_msg = Messages.query.filter_by(
            receiver_id=receiver_id,
            sender_id=sender_id).all()

        if receive_msg:
            messages = []

            for mesg in receive_msg:
                if last_time < mesg.time:
                    messages.append(mesg.message)

            return jsonify({
                'messages': messages
            })

        else:

            return jsonify({
                'messages': 'No message'
            })


@app.route('/add_last_visit', methods=['GET', 'POST'])
def add_last_visit():
    if request.method == 'POST':
        last_visit_info = request.get_json(force=True)
        user_id = last_visit_info['user_id']
        last_time = last_visit_info['time']

        last_visit_time = Visits(user_id=user_id, time=last_time)
        db.session.add(last_visit_time)
        db.session.flush()
        db.session.commit()
    
    return 'ok'


@app.route('/get_last_visit', methods=['GET', 'POST'])
def get_last_visit():
    if request.method == 'POST':
        lt_info = request.get_json(force=True)
        user_id = lt_info['user_id']

        visits = Visits.query.filter_by(user_id=user_id).all()

        if visits:
            visit_time = max([visit.time for visit in visits])

            return jsonify({
                'last_visit_time': visit_time
            })

        else:

            return jsonify({
                    'last_visit_time': 0
                })


if __name__ == '__main__':
    app.run()
  