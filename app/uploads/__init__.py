from flask import Blueprint, send_from_directory
from configs.DevConfig import BASE_DIR
uploads = Blueprint('uploads', __name__, url_prefix='/uploads')

# 二手货相关的文件


@uploads.route('/sh/<filename>')
def get_sh_file(filename):
    return send_from_directory(BASE_DIR + '/sh', filename)
