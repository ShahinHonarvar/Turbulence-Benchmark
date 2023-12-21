import re
def return_n_smallest_chars(str_):
    str_ = re.sub(r'[^A-Za-z0-9]+', '', str_)
    return str_.split()[:7]
