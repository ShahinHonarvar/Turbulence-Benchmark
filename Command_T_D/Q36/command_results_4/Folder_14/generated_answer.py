import re
def filter_chars(str):
    return re.sub(r'<[A-Z][a-c]', '', str)
