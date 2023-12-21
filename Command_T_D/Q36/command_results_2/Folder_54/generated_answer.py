import re
def filter_chars(s):
    return re.sub(r'(.)\d((?<=39).)', r'\1', s)
