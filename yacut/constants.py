import string

LINK_REGEX = r'^[a-zA-Z\d]{1,16}$'
MAX_SHORT_ID_LENGTH = 16
MIN_SHORT_ID_LENGTH = 6
RANGE_GENERATE_UNIQUE_ID = 5
VALID_SYMBOLS = string.ascii_letters + string.digits