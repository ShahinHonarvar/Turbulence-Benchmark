import re
def filter_chars(s):
    return re.sub(r'(![A-T]{1})', '', s)
