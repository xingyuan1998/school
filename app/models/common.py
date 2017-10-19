import datetime
import time
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
