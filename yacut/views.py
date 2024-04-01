from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()

    if form.validate_on_submit():
        original, short = form.original_link.data, form.custom_id.data

        if not short:
            short = URLMap.get_unique_short_id()

        if URLMap.get_model_instance(short):
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)

        if URLMap.validate_short_id(short) is False:
            flash('Заданная вами ссылка не соответствует регистру.')
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
            'redirect_view'
        )
    return render_template('index.html', form=form)


@app.route('/<short_id>', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.get_model_instance(short_id)
    if url:
        return redirect(url.original)
    abort(404)
