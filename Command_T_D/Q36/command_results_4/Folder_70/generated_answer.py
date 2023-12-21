import re
def filter_chars(s):
    return re.sub(r'[^!~]{170,195}[^!~]', '', s)
