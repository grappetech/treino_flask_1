from flask import Blueprint, render_template

Home = Blueprint('site', __name__)


@Home.route('/')
@Home.route('/index.html')
def index():
    return render_template('index.html')
