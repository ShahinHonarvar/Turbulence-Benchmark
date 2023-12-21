import re
def return_n_smallest_chars(s):
    return re.findall("[A-Z]", s)[:11]
