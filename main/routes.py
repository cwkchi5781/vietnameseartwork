import secrets, os
from PIL import Image
from flask import url_for, render_template, flash, redirect, request
from main import app
from main import db, bcrypt
from main.forms import SignUpForm, LoginForm, UpdateAccount, AddSection, AdminVerify
from main.models import User, Section, Purchase, Item
from flask_login import login_user, current_user, logout_user, login_required
from main.adminInfo import userView, admin, sectionView, itemView, myImageView

@app.route('/')
def home():
    sections = Section.query
    return render_template('home.html')

