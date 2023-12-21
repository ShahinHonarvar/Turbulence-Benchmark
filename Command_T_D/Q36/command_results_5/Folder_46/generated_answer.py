import re
def filter_chars(s):
    return re.sub(r'(?i)(?P<c>[a-z]{2,5})', '', s)
