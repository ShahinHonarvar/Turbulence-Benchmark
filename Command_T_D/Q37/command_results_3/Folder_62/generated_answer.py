import re
def filter_chars(s):
    return re.sub(r'(I[a-z]{,8})', '', s)
