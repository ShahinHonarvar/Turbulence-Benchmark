import re
def filter_chars(s):
    return re.sub(r'([a-z])([a-z]23[a-z]83)', r'\1', s)
