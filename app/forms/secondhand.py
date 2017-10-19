from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateSH(FlaskForm):
    title = StringField(
        'title',
        validators=[DataRequired(), Length(max=128)]
    )
    content = TextAreaField(
        'content',
        validators=[DataRequired(), Length(max=512)]
    )
    # ago_price = StringField(
    #     'ago_price',
    #     validators=[DataRequired(), Length(max=64)]
    # )
    # now_price = StringField(
    #     'now_price',
    #     validators=[DataRequired(), Length(max=64)]
    # )
