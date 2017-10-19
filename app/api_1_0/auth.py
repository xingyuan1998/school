import json

import bson.json_util
from flask import Blueprint, jsonify, g, request
from werkzeug.security import generate_password_hash

from app.forms.user import RegForm
from app.models.user import User, Profile

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/user/reg/', methods=['GET', 'POST'])
def reg_user():
    form = RegForm()
    if form.validate_on_submit():
        user = User()
        user.student_id = form.student_id.data
        user.password_hash = generate_password_hash(form.password.data)
        user.email = request.args.get('email')
        profile = Profile()
        profile.school = '中国矿业大学'
        user.profile = profile
        user.token = user.generate_auth_token()
        user.save()
        user.set_user_id()
        return jsonify({
            'status': 200,
            'des': '注册成功',
            'token': user.generate_auth_token()
        })
    return jsonify({
        'status': 400,
        'des': '数据提交失败'
    })


@auth.route('/user/login/', methods=['POST'])
def login_user():
    form = RegForm()
    if form.validate_on_submit():
        user = User.objects(student_id=form.student_id.data).first()
        if user is None:
            return jsonify({
                'status': '400',
                'des': '该用户不存在'
            })
        if user.verify_password(password=form.password.data):
            user.update(token=user.generate_auth_token())
            user.save()
            return jsonify({
                'status': 200,
                'des': '登陆成功',
                'token': user.token
            })
        return jsonify({
            'status': 400,
            'des': '登陆失败'
        })
