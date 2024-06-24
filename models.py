from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    img = db.Column(db.String())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    __tablename__ = "users"

    email = db.Column(db.String)
    password = db.Column(db.String())
    role = db.Column(db.String())

    def __init__(self, username, password, role="Guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
