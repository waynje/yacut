from datetime import datetime
from random import choices
from string import ascii_letters, digits

from flask import flash

from yacut import db
from .constants import (MAX_SHORT_ID_LENGTH,
                        MIN_SHORT_ID_LENGTH,
                        RANGE_GENERATE_UNIQUE_ID)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp
        )

    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])

    def get_unique_short_id():
        for _ in range(MIN_SHORT_ID_LENGTH):
            short = ''.join(choices(
                ascii_letters + digits,
                k=MIN_SHORT_ID_LENGTH)
            )
            if URLMap.query.filter_by(short=short).first():
                continue
            return short
        flash('Не удалось сгенерировать ссылку.')

    def create_url(original, short):
        if not short:
            short = URLMap.get_unique_short_id()
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map