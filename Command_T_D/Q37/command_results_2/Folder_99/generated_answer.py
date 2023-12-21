import re
def filter_chars(s):
    return re.sub(r'(?!<\d{3})([tT]h)+', '', s)
