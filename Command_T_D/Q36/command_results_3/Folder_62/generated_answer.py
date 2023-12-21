import re
def filter_chars(s):
    return re.sub(r'(?i)[\u0063-\u0065][\u0030-\u0039]', r'*', s)
