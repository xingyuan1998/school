import bson
from flask import jsonify
from flask_mongoengine import Document
from mongoengine import ReferenceField, StringField, IntField, DateTimeField, BooleanField
from bson.json_util import dumps
from app.models.user import User
import json


class Comment(Document):
    d_id = StringField(max_length=128)
    author = ReferenceField(User)
    content = StringField()
    title = StringField(max_length=256)
    good = IntField()
    bad = IntField()
    create_time = DateTimeField()
    update_time = DateTimeField()
    # 这个评论是否是回复 如果是回复 肯定要回复相关的内容
    is_reply = BooleanField()
    # 保存上个回复的id
    last_reply = StringField()
    last_reply_content = StringField()
    # 保存上个用户
    reply = ReferenceField(User)
    '''
        设置id
    '''

    def set_id(self):
        i = ''
        ids = json.loads(bson.json_util.dumps(self.id))
        for name, value in ids.items():
            i = value
        self.update(d_id=i)

    def to_json(self):
        i = ''
        ids = json.loads(dumps(self.id))
        for name, value in ids.items():
            i = value
        json_con = {
            'comment_id': i,
            'author': self.author.name,
            'content': self.content,
            'title': self.title,
            'create_time': self.create_time,
            'update_time': self.update_time,

            'is_reply': self.is_reply,
            'reply_user': self.reply.user_id,
            'reply_user_name': self.reply.name,
            'last_reply': self.last_reply,
            'last_reply_content': self.last_reply_content
        }
        return json_con
