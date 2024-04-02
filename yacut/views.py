from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id, validate_short_id, get_model_instance


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()

    if form.validate_on_submit():
        original, short = form.original_link.data, form.custom_id.data

        if not short:
            short = get_unique_short_id()

        if get_model_instance(short):
            flash('Предложенный вариант короткой ссылки уже существует.',
                  'rejected')
            return render_template('index.html', form=form)

        if validate_short_id(short) is False:
            flash('Заданная вами ссылка не соответствует регистру.',
                  'rejected')
            return render_template('index.html', form=form)

        url = URLMap(
            original=original,
            short=short
        )
        db.session.add(url)
        db.session.commit()
        flash(
            url_for(
                'redirect_view', short_id=short, _external=True),
            'complete_link'
        )
    return render_template('index.html', form=form)


@app.route('/<short_id>', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    if url:
        return redirect(url.original)
