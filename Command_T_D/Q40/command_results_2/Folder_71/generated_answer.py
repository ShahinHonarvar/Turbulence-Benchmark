import re
def return_n_smallest_chars(str_):
    res = re.findall(r'[a-z]', str_)[:14]
    return res
