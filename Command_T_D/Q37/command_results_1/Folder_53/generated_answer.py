import re
def filter_chars(s):
    return re.sub(r'[^*j]{%83,%99}', '', s)
