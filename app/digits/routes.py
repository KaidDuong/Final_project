# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.digits import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
# from app.digits.models import HandDigits
import uuid
import os
#from keras.models import load_model

@blueprint.route('/digits')
@login_required
def index():
    
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    return render_template('digits.html',data={})

@blueprint.route('/digits', methods=['GET', 'POST'])
def upload():
    image = request.files['data']
    imageName = saveToImage(imageFile=image)
 
    # predict digits
    score = 90
    predict = 1

    print("test user---------",current_user.__getattr__(username))
    # add into the db
    # new_hand_digits = HandDigits(path = "upload/images/{}".format(imageName),
    #                             CreatedBy= )
    data = {'imagePath': "upload/images/{}".format(imageName), 'score': score, 'predict': predict }
    return render_template('digits.html',data=data)


def saveToImage(imageFile=None, extension='.png'):
    imageName = str(uuid.uuid4()) + extension
    basedir =os.path.abspath(os.path.dirname(__file__))
    imageDirectory = os.path.join(basedir, 'static', 'upload', 'images')
    imagePath = os.path.join(imageDirectory, imageName)
    imageFile.save(imagePath, buffer_size=16384)
    imageFile.close()
    # image = open(imagePath, "wb")
    # print("ok----------------",type(imageFile))
    # base64 = imageFile.decode('base64')
    # image.write(base64)
    # image.close()

    return imageName

@blueprint.route('/digits/<template>')
def route_template(template):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

@blueprint.route('/digits/<static>')
def route_static(static):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500
