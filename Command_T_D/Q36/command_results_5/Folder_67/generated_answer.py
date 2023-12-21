import re
def filter_chars(s):
    return re.sub(r'([a-z]{18,31})', '', s)
