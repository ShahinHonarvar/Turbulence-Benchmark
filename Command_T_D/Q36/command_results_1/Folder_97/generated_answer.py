import re
def filter_chars(s):
    return re.sub(r'(?!s)[a-z]cdeflgjklmnpqrstu', '', s)
