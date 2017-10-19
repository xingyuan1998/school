from .common import Common
from .user import User
from mongoengine import (
    StringField,
    ReferenceField,
    BooleanField,
    IntField)


class Secondhand(Common):
    '''
        记录是否被购买
    '''
    types = StringField()
    is_bought = BooleanField(default=False)
    buyer = ReferenceField(User)
    # 以前的价格
    ago_price = StringField()
    # 现在的价格
    now_price = StringField()
    status = IntField()
    def to_json(self, *args, **kwargs):
        json_obj = {
            'title':self.title,
            'content':self.content,
            'types': self.types,
            'ago_price': self.ago_price,
            'now_price': self.now_price,
            'is_bought': self.is_bought
        }