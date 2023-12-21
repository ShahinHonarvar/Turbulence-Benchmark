import re
def return_n_smallest_chars(s):
    return re.findall("[A-z]", s, flags=re.I)[-14:]
