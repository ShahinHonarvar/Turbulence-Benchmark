import re
def filter_chars(s):
    return re.sub(r"([A-Z])([a-z])([A-Z])([a-z])", r"O", s)
