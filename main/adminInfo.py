import os
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask import url_for, redirect
from flask_login import current_user
from flask_admin import Admin
from main.forms import AddSection
from wtforms import fields, widgets


from main import app

file_path = os.path.join(os.path.dirname(__file__), 'images')



class allIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.adminStatus != 0:
                return True
            else:
                return False
        else:
            return False
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('Login'))


admin = Admin(app, index_view=allIndexView())


class userView(ModelView, ):
    column_list = ('username', 'email', 'adminStatus')
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.adminStatus != 0:
                return True
            else:
                return False
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('Login'))
'''
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '{} {}'.format(existing_classes, "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()
'''
class sectionView(ModelView):

    form_overrides = {
        'tail': AddSection
    }
    create_template = 'addSection.html'
    edit_template = 'edit_page.html'

    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.adminStatus != 0:
                return True
            else:
                return False
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('Login'))

class itemView(ModelView):
    #column_list = ('id', 'name', 'section')

    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.adminStatus != 0:
                return True
            else:
                return False
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('Login'))
class myImageView(FileAdmin):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.adminStatus != 0:
                return True
            else:
                return False
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('Login'))
