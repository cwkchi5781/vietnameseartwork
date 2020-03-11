from flask import url_for, render_template, flash, redirect, request
from main import app


@app.route('/')
def home():
    return render_template('home.html')

