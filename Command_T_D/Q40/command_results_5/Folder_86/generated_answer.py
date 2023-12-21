import re
def return_n_smallest_chars(s):
    res = sorted(re.findall(r"[A-Z0-9]", s))[:34]
    return res
