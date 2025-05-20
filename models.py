from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    image_url = db.Column(db.String(200), nullable=True)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def init_db():
    db.drop_all()
    db.create_all()
    if not Product.query.first():
        db.session.add_all([
            Product(name='Ноутбук ASUS', price=55000, image_url='https://via.placeholder.com/150'),
            Product(name='Смартфон Samsung', price=35000, image_url='https://via.placeholder.com/150'),
            Product(name='Наушники JBL', price=5000, image_url='https://via.placeholder.com/150')
        ])
    db.session.commit()
