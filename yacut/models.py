from datetime import datetime
import random
from urllib.parse import urlparse

from yacut import db
from .constants import (MAX_SHORT_ID_LENGTH,
                        MIN_SHORT_ID_LENGTH,
                        VALID_SYMBOLS)


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
        short = ''.join(random.choice(VALID_SYMBOLS)
                        for _ in range(MIN_SHORT_ID_LENGTH))
        return short

    def validate_url(url):
        parsed_url = urlparse(url)
        if parsed_url.scheme in ['http', 'https', 'ftp'] and parsed_url.netloc:
            return True
        return False

    def validate_short_id(short_id):
        if len(short_id) > MAX_SHORT_ID_LENGTH:
            return False
        for char in short_id:
            if char not in VALID_SYMBOLS:
                return False
        return True

    def short_id_exists(self, short_id):
        return bool(self.query.filter_by(short=short_id).first())

    def create_model_instance(original, short_id):
        if short_id is None:
            short_id = URLMap.get_unique_short_id()
        url = URLMap(original=original, short=short_id)
        db.session.add(url)
        db.session.commit()
        return url

    def get_model_instance(short_id):
        return URLMap.query.filter_by(short=short_id).first()