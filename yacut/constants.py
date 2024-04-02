import string

LINK_REGEX = r'^[a-zA-Z\d]{1,16}$'
MAX_SHORT_ID_LENGTH = 16
MIN_SHORT_ID_LENGTH = 6
VALID_SYMBOLS = string.ascii_letters + string.digits