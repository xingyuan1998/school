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

    '''
        得到二手货的序列化结果
    '''
    def get_json(self):
        data_comment = []
        for comment in self.comments:
            data_comment.append(comment.to_json())
        json_obj = {
            'title':self.title,
            'content':self.content,
            'types': self.types,
            'ago_price': self.ago_price,
            'now_price': self.now_price,
            'is_bought': self.is_bought,
            'comments': data_comment,
            'author': self.author.name,
            'author_id': self.author.user_id
        }
        return json_obj
