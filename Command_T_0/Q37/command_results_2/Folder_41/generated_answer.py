import re
def filter_chars(s):
    return re.sub(r'[A-Z][^A-Z]V[A-Z][^A-Z]o', '', s)
