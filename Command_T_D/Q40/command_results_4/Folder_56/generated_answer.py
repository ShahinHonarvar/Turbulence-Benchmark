import re
def return_n_smallest_chars(s):
    r = re.findall(r'[A-z]', s)
    return r[:21]
