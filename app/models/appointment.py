from .common import Common
from .user import User
from mongoengine import (IntField,
                         ListField,
                         ReferenceField,
                         EmbeddedDocument,
                         DateTimeField,
                         EmbeddedDocumentField)


class Member(EmbeddedDocument):
    user = ReferenceField(User)
    join_time = DateTimeField()


class Appointment(Common):
    starter = ReferenceField(User)
    size = IntField()
    member = ListField(EmbeddedDocumentField(Member))
    start_time = DateTimeField()
    end_time = DateTimeField()
