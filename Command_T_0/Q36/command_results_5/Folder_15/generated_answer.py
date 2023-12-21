import re
def filter_chars(s):
    return re.sub(r'(?!\A)[^h-k](?!\Z)[^h-k]', '', s)
