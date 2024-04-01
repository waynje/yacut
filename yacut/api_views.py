from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=('POST',))
def add_short_url():
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    url = data.get('url')
    short_link = data.get('custom_id')
    if not URLMap.validate_url(url):
        raise InvalidAPIUsage(
            'Введите корректный URL адрес')

    if short_link:
        if URLMap.get_model_instance(short_link):
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )
        if URLMap.validate_short_id(short_link) is False:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
    else:
        short_link = URLMap.get_unique_short_id()
    new_url = URLMap(original=url, short=short_link)
    db.session.add(new_url)
    db.session.commit()
    return jsonify({
        'url': new_url.original,
        'short_link': url_for('index_view', _external=True) + new_url.short
    }), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.get_model_instance(short_id)
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    if not URLMap.validate_short_id(short_id):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки')
    return jsonify({'url': url.original}), 200