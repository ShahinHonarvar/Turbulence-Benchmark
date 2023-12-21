import re
def return_n_smallest_chars(s):
    return re.findall(r"[A-Za-z]", s)[-46:]
