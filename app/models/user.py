import datetime
from untils import get_hash, check_hash
from configs.DevConfig import SECRET_KEY
from exts import db
from flask import current_app, jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from mongoengine import (
    StringField,
    IntField,
    EmailField,
    Document,
    DynamicDocument,
    EmbeddedDocumentField,
    EmbeddedDocument,
    ListField,
    DateTimeField,

)

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Follower(db.EmbeddedDocument):
    user_id = StringField(max_length=128)
    student_id = StringField(max_length=64)
    name = StringField(max_length=64)
    time = DateTimeField(default=datetime.datetime.now())
    meta = {'allow_inheritance': True}


class Followers(Follower):
    pass


class Interests(Follower):
    pass


class Profile(db.EmbeddedDocument):
    birthday = DateTimeField()
    collage = StringField(max_length=128)
    school = StringField(max_length=128)
    qq = StringField(max_length=128)
    wechat = StringField(max_length=128)
    major = StringField(max_length=128)


class User(db.Document):
    student_id = StringField(max_length=64)
    # 用户登陆令牌
    token = StringField(max_length=256)
    # 真实姓名
    name = StringField(max_length=64)
    # 昵称
    nick_name = StringField(max_length=64)
    # 密码的hash值
    password_hash = StringField(max_length=256)
    # 1表示男生，2 表示女生3表示保密 或未设置吧
    sex = IntField(default=3)
    email = EmailField()
    # 个人简介
    profile = EmbeddedDocumentField(Profile)
    # 粉丝
    followers = ListField(EmbeddedDocumentField(Followers))
    # 关注者
    intersts = ListField(EmbeddedDocumentField(Interests))
    # 不让他看自己的朋友圈或者什么玩意的
    block_circles = ListField(StringField(max_length=128))
    # 不让他看所有的社交
    block_all = ListField(StringField(max_length=128))
    # 不看某人的朋友圈名单
    ignore_circles = ListField(StringField(max_length=128))
    # 不看某人的全部社交相关
    ignore_all = ListField(StringField(max_length=128))

    '''

        状态 >0 表示正常
        <=0 说明不正常
        1 表示正常
        -1 尚未认证成功（正在认证）
        -2 认证失败
        -3 被举报

    '''
    status = IntField()
    create_time = DateTimeField()
    update_time = DateTimeField()

    def generate_auth_token(self):
        self.token = get_hash(self.student_id + str(datetime.datetime.now()))
        return self.token

    def verify_auth_token(self, token):
        return check_hash(self.token, token)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

