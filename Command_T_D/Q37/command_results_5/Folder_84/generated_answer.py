import re
def filter_chars(s):
    return re.sub(r'[^A-6][138:920]', '', s)
