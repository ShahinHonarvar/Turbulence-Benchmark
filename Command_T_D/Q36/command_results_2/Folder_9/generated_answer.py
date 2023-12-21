import re
def filter_chars(s):
    return re.sub(r'[^A-Q]{%50,92}', '', s)
