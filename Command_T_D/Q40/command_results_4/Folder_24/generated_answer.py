import re
def return_n_smallest_chars(s):
    return re.findall("[a-z]", s)[-32:]
