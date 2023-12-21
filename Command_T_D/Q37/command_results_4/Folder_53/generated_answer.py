import re
def filter_chars(s):
    return re.sub(r'([*][^j]*)(?<=\s*[A-Z][^A-Z]*[A-Z])', r'\1', s)
