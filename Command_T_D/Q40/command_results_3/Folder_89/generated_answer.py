import re
def return_n_smallest_chars(str_of_chars):
    str_of_chars = re.sub(r'[^A-z]','',str_of_chars)
    n_smallest_chars = sorted(set(str_of_chars))[:55]
    return n_smallest_chars
