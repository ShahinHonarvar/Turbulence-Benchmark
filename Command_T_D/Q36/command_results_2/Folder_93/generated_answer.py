import re
def filter_chars(s):
    return re.sub(r'[^&c]{%52,88}', '', s)
