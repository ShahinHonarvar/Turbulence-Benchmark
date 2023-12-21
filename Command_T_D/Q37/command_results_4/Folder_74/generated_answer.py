import re
def filter_chars(s):
    return re.sub(r'([fho])([19-32])', r'\1', s)
