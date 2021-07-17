from flask import Blueprint, render_template, Request, Response, redirect, url_for, request

from erp.models.user import User
from erp.repositories.user_repository import UserRepository
from utils import util

Auth = Blueprint('auth', __name__)


@Auth.route('/login', methods=['GET'])
def login():
    if UserRepository().get_one(1) == False:
        user = User()
        user.set_name('Administrator')
        user.set_username('admin')
        user.set_password('admin')
        user.set_email('admin@erp.com')
        user.set_phone('')
        user.set_active(True)
    return render_template('auth/login.html')


@Auth.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if UserRepository().validate(username, password):
        return redirect(url_for('site.index'))
    else:
        return render_template('auth/login.html')


@Auth.route('/recover', methods=['GET'])
def recover():
    return render_template('auth/recover.html')


@Auth.route('/register', methods=['GET'])
def register():
    return render_template('auth/register.html')
