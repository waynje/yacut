from random import choices
import re
from string import ascii_letters, digits

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .constants import MAX_SHORT_ID_LENGTH, LINK_REGEX
from .forms import URLForm
from .models import URLMap
from .utils import return_to_index


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()

    if not form.validate_on_submit():
        return_to_index()

    original, short = form.original_link.data, form.custom_id.data

    if URLMap.query.filter_by(short=short).first() is not None:
        flash(f'Предложенный вариант короткой ссылки уже существует.')
        return_to_index()

    if (short != '' and short is not None and not re.match(LINK_REGEX, short)):
        flash('Недопустимое имя для ссылки.')
        return_to_index()

    url_map = URLMap.create_url(original, short)
    return render_template(
        'index.html',
        form=form,
        result_url=url_for('index_view', _external=True) + url_map.short
    )

