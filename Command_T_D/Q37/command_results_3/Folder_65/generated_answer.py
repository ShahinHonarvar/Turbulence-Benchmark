import re
def filter_chars(s):
    return re.sub(r'[\d]{1,2}|\w|/|,|&|_', '', s, flags=re.I)
