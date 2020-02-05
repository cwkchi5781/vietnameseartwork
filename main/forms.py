from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from main.models import User
from flask_login import current_user


#SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=4), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a new one')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This email has already been used.')

class UpdateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    profile_img = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists. Please choose a new one')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('This email has already been used.')



class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class AddSection(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    img_file = FileField('Upload image', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Add Section')

    def validate_name(self, name):
        section = User.query.filter_by(name=name.data).first()
        if section:
            raise ValidationError('Name is already used by another section')

    def validate_img(self, img_file):
        img = User.query.filter_by(img_file=img_file.data).first()
        if img:
            raise ValidationError('The image is already in use.')
