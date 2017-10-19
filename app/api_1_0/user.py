from flask import request, url_for, jsonify, g
import json
from app.api_1_0 import api
from app.forms.user import RegForm
from app.models.news import News
from app.models.user import User, Profile
from werkzeug.security import generate_password_hash
from itsdangerous import JSONWebSignatureSerializer as Serializer


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




@api.route('/show/user/')
def users():
    # 注册的时候需要吧profile 注册好
    # 否则不好处理现在的数据
    return jsonify(g.user)

@api.route('/del/user/')
def us():
    user = User.objects.all()
    user.delete()
    return 'successful del'

@api.route('/test/')
def test():
    s = Serializer('ttttt')
    return jsonify(s.dumps({"id":'123'}))





