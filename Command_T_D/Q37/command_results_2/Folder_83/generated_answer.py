import re
def filter_chars(s):
    return re.sub(r'([a-z]{29,79})', '', s)
