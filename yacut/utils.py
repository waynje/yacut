import random
from urllib.parse import urlparse

from .constants import VALID_SYMBOLS, MIN_SHORT_ID_LENGTH, MAX_SHORT_ID_LENGTH
from .models import URLMap


def get_unique_short_id():
    return ''.join(random.choice(VALID_SYMBOLS)
                   for _ in range(MIN_SHORT_ID_LENGTH))


def validate_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https', 'ftp'] and parsed_url.netloc


def validate_short_id(short_id):
    if len(short_id) > MAX_SHORT_ID_LENGTH:
        return False
    for char in short_id:
        if char not in VALID_SYMBOLS:
            return False
    return True


def get_model_instance(short_id):
    return URLMap.query.filter_by(short=short_id).first()