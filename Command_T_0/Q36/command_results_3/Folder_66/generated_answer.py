import re
def filter_chars(s):
    return re.sub(r'[^!}]{39,87}', '', s)
