import re
def filter_chars(s):
    return re.sub(r'(H[a-z]{5})', '', s)
