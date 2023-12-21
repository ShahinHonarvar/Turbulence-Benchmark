import re
def return_n_smallest_chars(s):
    str_list = sorted(re.findall(r"[a-z]", s))[:28]
    return str_list
