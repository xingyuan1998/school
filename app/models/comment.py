from flask import jsonify
from flask_mongoengine import Document
from mongoengine import ReferenceField, StringField, IntField, DateTimeField

from app.models.user import User


class Comment(Document):
    author = ReferenceField(User)
    content = StringField()
    title = StringField(max_length=256)
    good = IntField()
    bad = IntField()
    create_time = DateTimeField()
    update_time = DateTimeField()

    def to_json(self):
        json_con ={
            'comment_id': str(self.id),
            'author': self.author.name,
            'content': self.content,
            'title': self.title,
            'create_time': self.create_time,
            'update_time': self.update_time
        }
        return json_con
