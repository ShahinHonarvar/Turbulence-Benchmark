import re
def filter_chars(s):
    return re.sub(r'[^\dA-Z0-9_]{%48{%75}}'.format(len(s)), '', s)
