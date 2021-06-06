from Customer_Churn import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    print(id)
    username = db.Column(db.String(64),unique=True,index=True)
    print(username)
    password_hash = db.Column(db.String(128))
    print(password_hash)

    def __init__(self,username,password):
        self.username = username
        self.password_hash = generate_password_hash(password)
        print('added user or updated')

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"
