from main import db, login_manager, admin
from datetime import datetime
from flask_login import UserMixin
from flask_admin import Admin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    img_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    purchase = db.relationship('Purchase', backref='user', lazy=True)

    def __repr__(self):
        return f"Username('{self.username}'), Email('{self.email}'), Image('{self.img_file}')"


#class Admin(db.Model, Admin):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(20), unique=True, nullable=False)
#    #email = db.Column(db.String(120), unique=True, nullable=False)
#    #img_file = db.Column(db.String(20), nullable=False, default="default.jpg")
#    #password = db.Column(db.String(60), nullable=False)

#    def __repr__(self):
#        return f"Username('{self.username}'), Email('{self.email}'), Image('{self.img_file}')"


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    img_file = db.Column(db.String(150), nullable=False, default="default.jpg")
    img_alt = db.Column(db.String(200), nullable=False, default="Image")
    item = db.relationship('Item', backref='section', lazy=True)

    def __repr__(self):
        return f"User('{self.name}'), Image('{self.img_file}', Img-alt('{self.img_alt}')"


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.DECIMAL(7, 2))
    date_bought = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('Item', backref='purchase', lazy=True)

    def __repr__(self):
        return f"Cost('{str(self.cost)}'), User ID: ('{self.user_id}')"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    cost = db.Column(db.DECIMAL(6, 2))
    item_img = db.Column(db.String(20), nullable=False, default="default.jpg")
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)

    def __repr__(self):
        return f"Cost('{str(self.name)}'), User ID: ('{self.cost}')"

