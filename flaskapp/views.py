from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from flaskapp import settings


blueprint = Blueprint(settings.appnamed, __name__)


@blueprint.route('/')
def home():
    return render_template('public/index.html')
