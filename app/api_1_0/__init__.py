from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from . import (
    appointment,
    auth,
    circles,
    news,
    profess,
    roommate,
    secondhand,
    tasks,
    user
)
@api.route('/')
def hello():
    return 'dddd'
