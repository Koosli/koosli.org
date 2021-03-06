# -*- coding: utf-8 -*-

import os

from flask import Blueprint, render_template, send_from_directory, abort, flash, url_for, redirect, request
from flask import current_app as APP, make_response
from flask.ext.login import login_required, current_user, login_user, logout_user

from .models import User, UserStats
from .forms import RegistrationForm, PreferenceForm
from koosli import db


mod = Blueprint('user', __name__, url_prefix='')


@mod.route('/profile')
@login_required
def index():
    '''The user dashboard where stats can be seen and preferences changed'''

    stats =  UserStats.query.filter_by(id=current_user.user_stats_id).first()
    return render_template('user_dash.html', user=current_user, stats=stats)


@mod.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('user_login.html')

    email = request.form['email']
    password = request.form['password']
    registered_user = User.query.filter_by(email=email).first()

    if registered_user is None:
        flash('This email does not belong to a registered user' , 'error')
        return render_template('user_login.html'), 400

    if not registered_user.check_password(password):
        flash('Wrong password or username' , 'error')
        return render_template('user_login.html'), 401

    login_user(registered_user)
    return redirect(request.args.get('next') or '/profile')


@mod.route('/register' , methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    splash_registration = APP.config.get('SPLASH_REGISTRATION')

    if request.method == 'GET':
        return render_template('user_register.html', form=form)

    if not form.validate():
        return render_template('user_register.html', form=form), 400

    stats = UserStats()
    user = User(email=form.email.data, password=form.password.data, user_stats=stats)
    db.session.add(user)
    db.session.add(stats)
    db.session.commit()
    login_user(user)

    return redirect(url_for('user.index'))


@mod.route('/interest' , methods=['GET','POST'])
def interest():
    form = RegistrationForm(request.form)
    splash_registration = APP.config.get('SPLASH_REGISTRATION')

    if request.method == 'GET':
        return render_template('splash.html', form=form)

    if not form.validate():
        return render_template('splash.html', form=form), 400

    stats = UserStats()
    user = User(email=form.email.data, password=form.password.data, user_stats=stats)
    db.session.add(user)
    db.session.add(stats)
    db.session.commit()
    login_user(user)

    flash('Takk for interessen!', 'info')
    return redirect('/')


@mod.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@mod.route('/preference' , methods=['POST'])
@login_required
def preference():
    form = PreferenceForm(request.form)

    if not form.validate():
        abort(400)

    stats = UserStats.query.filter_by(id=current_user.user_stats_id).update({
        'beneficiary': form.beneficiary.data,
        'search_provider': form.search.data,
        'ad_network': form.ads.data,
        'advertising_off': form.advertising_off.data
    })
    db.session.commit()

    return make_response('Preference updated', 200)
