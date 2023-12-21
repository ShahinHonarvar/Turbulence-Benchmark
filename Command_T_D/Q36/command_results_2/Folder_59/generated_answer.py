import re
def filter_chars(s):
    return re.sub(r'(?!\?)([a-z])([^a-z\?]{%d}){%d}(?!k)', r'\1', s)
