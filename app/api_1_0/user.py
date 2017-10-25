import os
from flask import request, url_for, jsonify, g, send_from_directory
import json

from werkzeug.utils import secure_filename

from app.api_1_0 import api
from app.forms.user import RegForm, ChangePwdForm
from app.models.news import News
from app.models.user import User, Profile
from werkzeug.security import generate_password_hash
from itsdangerous import JSONWebSignatureSerializer as Serializer

from configs.DevConfig import BASE_DIR
from untils import allowed_file, get_time_hash


@api.before_request
def before():
    token = request.values.get('token')
    if token is None:
        return jsonify({
            'status': 400,
            'des': '请求失败'
        })
    user = User.objects(token=token).first()
    if user is None:
        return jsonify({
            'status': 400,
            'des': 'token请求失败'
        })
    g.user = user


# 更换头像
@api.route('/user/avatar/', methods=['POST'])
def change_avatar():
    image = request.files.get('avatar')
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        name = get_time_hash(filename) + "." + filename.rsplit('.', 1)[1]
        user = g.user
        user.update(avatar=name)
        image.save(os.path.join(BASE_DIR + '/avatar', name))
        return jsonify({
            'status': 200,
            'avatar': send_from_directory(BASE_DIR + '/avatar', name),
            'des': '上传头像成功'
        })
    return jsonify({
        'status': 400,
        'des': '更改头像失败'
    })


# 修改密码
@api.route('/password/', methods=['POST'])
def change_pwd():
    form = ChangePwdForm()
    if form.validate_on_submit():
        if g.user.verify_password(form.last_pwd.data):
            g.user.set_password()
            g.user.save()
            return jsonify({
                'status': 200,
                'des': '修改成功',
                'token': g.user.generate_auth_token()
            })
        return jsonify({
            'status': 400,
            'des': '密码错误'
        })
    return jsonify({
        'status': 400,
        'des': '请求错误'
    })




# 得到当前用户的简介信息
@api.route('/show/user/')
def users():
    # 注册的时候需要吧profile 注册好
    # 否则不好处理现在的数据
    return jsonify(g.user.to_json())


@api.route('/del/user/')
def us():
    user = User.objects.all()
    user.delete()
    return 'successful del'
