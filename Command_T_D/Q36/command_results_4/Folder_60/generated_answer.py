import re
def filter_chars(s):
    return re.sub(r'([a-zA-Z])\b(g-o)\b([a-zA-Z])', r'\1\2\3', s)
