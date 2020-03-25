import secrets, os
from flask_admin.contrib.sqla import ModelView
from PIL import Image
from flask import url_for, render_template, flash, redirect, request
from main import app
from main.forms import SignUpForm, LoginForm, UpdateAccount, AddSection, review
from main import db, bcrypt, admin
from main import db, bcrypt, admin
from main.forms import SignUpForm, LoginForm, UpdateAccount, AddSection
from main.models import User, Section, Purchase, Item
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    sections = Section.query.all()
    return render_template('sectionsDisplay.html', sections=sections)

@app.route('/signUp', methods=['GET', 'POST'])
def SignUp():
    if current_user.is_authenticated:
        flash("You are already logged in", 'warning')
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {form.username.data}! You can now log in', 'success')
        return redirect(url_for('Login'))
    return render_template('signUp.html', form=form, title='Sign Up')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        flash("You are already logged in", 'warning')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        euser = User.query.filter_by(email=form.email.data).first()
        #nuser = User.query.filter_by(email=form.email.data).first()

        if euser and bcrypt.check_password_hash(euser.password, form.password.data):
            flash(f'{euser.username}! logged in', 'success')
            login_user(euser, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            #if next_page:
            #    return redirect(url_for(next_page))
            #else:
            #    return redirect(url_for('home'))
        else:
            flash('Failed Login. Please check email and password', 'danger')
    return render_template('logIn.html', form=form, title='Log In')


@app.route('/logout', methods=['GET', 'POST'])
def logOut():
    logout_user()
    form = review()
    return render_template('review.html', form=form, title='Reviews')

@app.route('/reviews')
def reviewPage():
    pass

def save_picture(form_picture, profile):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + f_ext
    while User.query.filter_by(img_file=picture_fn).first():
        random_hex = secrets.token_hex(8)
        picture_fn = random_hex + f_ext
    if profile:
        picture_path = os.path.join(app.root_path, 'static/images/profile_pics/', picture_fn)
    else:
        picture_path = os.path.join(app.root_path, 'static/images/', picture_fn)

    output_size = (140, 140)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    print(picture_path)
    return picture_fn



@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.profile_img.data:
            previous_url = app.root_path + "/static/images/profile_pics/" + current_user.img_file
            try:
                os.unlink(previous_url)
                print("% s removed successfully" % previous_url)
            except OSError as error:
                print(error)
                print("File path can not be removed")
            profile_pic = save_picture(form.profile_img.data, True)
            current_user.img_file = profile_pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('You account has been updated.', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    img_file = url_for('static', filename='images/profile_pics/' + current_user.img_file)
    return render_template('account.html', title='Profile', img_file=img_file, form=form)


@app.route('/admin')
def admin():
    admin.add_view(ModelView(User, db.session))
    #return render_template('sectionsDisplay.html')

@app.route('/admin/addSection', methods=['GET', 'POST'])
def addSection():
    form = AddSection()
    if form.validate_on_submit():
        if form.img_file.data:
            imgfile = save_picture(form.img_file.data, False)
            sect = Section(name=form.name.data, img_alt=form.img_alt.data, img_file=imgfile)
        else:
            sect = Section(name=form.name.data, img_alt=form.img_alt.data)
        db.session.add(sect)
        db.session.commit()
        flash(f'Section {form.name.data} created', 'success')
    return render_template('admin/addSection.html', form=form)

app.route('/purchases/new')
def checkOut():
    return render_template('purchase.html')


@app.route('/section/<sectionName>/catlog')
def sectionPage(sectionName):
    return render_template('sectionsOutline.html', section=sectionName)

@app.route('/section/<sectionName>/<item>')
def item(sectionName, item):
    return render_template('itemOutline.html', section=sectionName, item=item)





