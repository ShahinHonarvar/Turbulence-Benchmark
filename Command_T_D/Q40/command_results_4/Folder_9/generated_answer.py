import re
def return_n_smallest_chars(s):
    res = re.findall(r"[A-Z]", s)
    return res[:20]
