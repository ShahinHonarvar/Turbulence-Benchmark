import re
def filter_chars(s):
    return re.sub(r'[+\d]{%21,%43}', '', s)
