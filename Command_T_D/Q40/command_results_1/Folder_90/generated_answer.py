import re
def return_n_smallest_chars(s):
    res = re.findall(r'[a-z]', s)[:24]
    return res
