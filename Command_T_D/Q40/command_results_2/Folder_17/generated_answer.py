import re
def return_n_smallest_chars(s):
    return sorted(re.findall("[A-Z]", s), key=str.lower)[:11]
