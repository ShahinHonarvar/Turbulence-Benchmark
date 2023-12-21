import re
def filter_chars(s):
    return re.sub(r'(t<|v>)', '', s, flags=re.I)
