import re
def filter_chars(s):
    return re.sub(r'([^Ys]?)', '', s, flags=re.I)
