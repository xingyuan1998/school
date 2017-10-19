import datetime
import json
import time

import bson.json_util
from mongoengine import (
    StringField,
    IntField,
    EmailField,
    Document,
    DynamicDocument,
    EmbeddedDocumentField,
    EmbeddedDocument,
    ListField,
    BooleanField,
    DateTimeField,
    ReferenceField,
)

from app.models.comment import Comment
from .user import User



class Common(Document):
    d_id = StringField(max_length=128)
    author = ReferenceField(User)
    title = StringField(max_length=256)
    content = StringField()
    # 内容之中图片列表
    pictures = ListField(StringField(max_length=256))
    # 浏览量
    watch_num = IntField(default=23)
    # 好
    good = IntField(default=0)
    # 坏
    bad = IntField(default=0)
    # 内容里面的讨论
    comments = ListField(ReferenceField(Comment))
    # 创建时间
    create_time = DateTimeField(default=datetime.datetime.now())
    # 更新时间
    update_time = DateTimeField()
    meta = {'allow_inheritance': True}

    def set_id(self):
        i = ''
        ids = json.loads(bson.json_util.dumps(self.id))
        for name, value in ids.items():
            i = value
        self.update(d_id=i)
