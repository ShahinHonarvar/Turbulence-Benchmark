import re
def filter_chars(s):
    return re.sub(r'(?!s)[A-Z][a-z]{40}(?!s)', '', s)
