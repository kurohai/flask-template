from flask import Blueprint
from flask import render_template, request, url_for
from flaskapp import *


blueprint = Blueprint(flasktemplate.appnamed, __name__)

@blueprint.route('/')
def home():
    return render_template('public/index.html')
