from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    pass_secure = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')
    

    @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


     def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):

       return f'User {self.username}'

class Pitch (db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    post = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='pitch',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    

    def __repr__(self):
        return f'User {self.name}'