import hashlib

import time

from configs import DevConfig


def get_hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def get_time_hash(s):
    return hashlib.md5((s+str(time.time())).encode('utf-8')).hexdigest()



def check_hash(s1, s2):
    return s1 == get_hash(s2)

'''
    允许上传的文件后缀

'''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in DevConfig.ALLOWED_EXTENSIONS
