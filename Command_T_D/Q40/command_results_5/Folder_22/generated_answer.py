import re
def return_n_smallest_chars(s):
    x = list(sorted(re.findall(r'[a-z]', s)))[:76]
    return x
