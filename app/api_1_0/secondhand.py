import datetime
import json
import time

import os
from flask import request, g, jsonify
from werkzeug.utils import secure_filename

from app.api_1_0 import api
from app.forms.secondhand import CreateSH
from app.models.common import Comment
from app.models.secondhand import Secondhand
from app.models.user import User
from configs import DevConfig
from configs.DevConfig import BASE_DIR
from untils import get_hash, get_time_hash, allowed_file

'''

1. 显示当前的二手货列表（获取是否点赞的字段）
2. 显示用户的二手活列表（购买的二手货，出售的二手货）
4. 评论二手货
5. 删除二手货 需要判断是否有权限 是否是当前用户的二手货
6. 设置二手货已经售卖。 

'''

# 显示所有的二手货
@api.route('/sh/list/<int:page>/')
def sh_list(page=1):
    per_page = 10
    pre = int(page-1)*per_page
    nex = page * per_page
    shs = Secondhand.objects[pre:nex]
    datas = []
    for sh in shs:
        datas.append(sh.get_json())
    return jsonify(datas)

# 购买的
@api.route('/sh/buy/list/<int:page>/')
def sh_buy_list(page=1):
    per_page = 10
    pre = int(page-1)*per_page
    nex = page * per_page
    sh = Secondhand.objects(author=g.user)[pre:nex]
    if sh is None or len(sh) == 0:
        return jsonify({
            'status': 400,
            'des': '暂无数据'
        })
    data = []
    for s in sh:
        data.append(s.get_json)
    return jsonify(data)

# 已经卖出的
@api.route('/sh/bought/list/<int:page>/')
def sh_bought_list(page=1):
    per_page = 10
    pre = int(page-1)*per_page
    nex = page * per_page
    shs = Secondhand.objects(buyer=g.user)[pre:nex]
    if shs is None or len(shs)==0:
        return jsonify({
            'status': 400,
            'des': '暂无数据'
        })
    datas = []
    for sh in shs:
        datas.append(sh.get_json())
    return jsonify(datas)

# 创建一个评论
@api.route('/sh/comments/', methods=['POST'])
def create_comments():
    sh_id = request.values.get('sh_id')
    sh = Secondhand.objects(id=sh_id).first()
    if sh is None:
        return jsonify({
            'status':404,
            'des':'没有找到这个二手货'
        })

    comment = Comment()
    comment.author = g.user
    comment.title = request.values.get('title')
    comment.content = request.values.get('content')
    is_reply = request.values.get('is_reply')
    if is_reply == 1:
        comment.is_reply = True
        last_id = request.values.get('last_id')
        last_comment = Comment.objects(id=last_id).first()
        if last_comment is None:
            return jsonify({
                'status': 400,
                'des': 'dddddd'
            })
        comment.last_reply = last_comment.d_id
    comment.create_time = datetime.datetime.now()
    comment.save()
    comment.set_id()
    sh.comments.append(comment)
    sh.save()
    return jsonify(comment)

# 删除评论
@api.route('/sh/comments/', methods=['DELETE'])
def del_comments():
    comment_id = request.values.get('comment_id')
    comment = Comment.objects(id=comment_id).first()
    if comment is None:
        return jsonify({
            'status': 404,
            'des': '没有找到'
        })
    if comment.author == g.user:
        Secondhand.objects(comments=comment).update(pull__comments = comment)
        return jsonify({
            'status': 200,
            'des': '成功删除'
        })
    else:
        return jsonify({
            'status': 400,
            'des': '没有权限'
        })

# 删除二手货
@api.route('/sh/', methods=['DELETE'])
def del_sh():
    sh_id = request.values.get('sh_id')
    if sh_id is None:
        return jsonify({
            'status': 404,
            'des': '没有找到'
        })
    sh = Secondhand.objects(id=sh_id).first()
    if sh is None:
        return jsonify({
            'des':'没有找到该二手货'
        }), 404
    sh.delete()
    return 'del ok'

# 删除所有的二手货 方便测试
@api.route('/shs/', methods=['DELETE'])
def del_all_sh():
    sh = Secondhand.objects.all()
    sh.delete()
    return jsonify({
        'ok': 'ok'
    })


# 新建一个二手货
@api.route('/sh/', methods=['GET', 'POST'])
def create_sh():
    form = CreateSH()
    if form.validate_on_submit():
        sh = Secondhand()
        sh.title = form.title.data
        sh.content = form.content.data
        sh.ago_price = request.values.get('ago_price')
        sh.now_price = request.values.get('now_price')
        sh.types = request.values.get('types')
        sh.author = g.user
        # 上传图片的相关处理
        files = request.files.getlist('file')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                name = get_time_hash(filename)+"."+filename.rsplit('.', 1)[1]
                sh.pictures.append(name)
                file.save(os.path.join(BASE_DIR + '/sh', name))
        sh.save()
        sh.set_id()
        return jsonify(sh.get_json())
