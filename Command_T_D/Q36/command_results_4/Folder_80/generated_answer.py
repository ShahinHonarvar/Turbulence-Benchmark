import re
def filter_chars(s):
    return re.sub(r'<[a-z]>([j-m])<[a-z]', r'\1', s)
