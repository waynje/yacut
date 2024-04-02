from typing import Final

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import LINK_REGEX

MIN_LENGTH: Final = 1
MAX_LENGTH: Final = 16


class URLForm(FlaskForm):
    original_link = URLField(
        'Вставьте длинную ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректная ссылка')
        ]
    )
    custom_id = StringField(
        'Введите короткую ссылку',
        validators=[
            Optional(),
            Length(MIN_LENGTH, MAX_LENGTH),
            Regexp(
                regex=LINK_REGEX,
                message='Допустимы только буквы a-z и цифры.'
            )
        ]
    )
    submit = SubmitField()