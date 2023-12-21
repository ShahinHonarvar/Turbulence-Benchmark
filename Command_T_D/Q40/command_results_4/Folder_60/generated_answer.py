import re
def return_n_smallest_chars(s):
    x = sorted(re.findall(r'[a-z]', s))[:28]
    return x
