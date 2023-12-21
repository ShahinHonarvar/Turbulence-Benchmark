import re
def filter_chars(s):
    return re.sub(r'(?<=\A[^*])\w+|(?<=\s)\w+', '', s)
