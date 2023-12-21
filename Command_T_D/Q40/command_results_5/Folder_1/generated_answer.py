import re
def return_n_smallest_chars(s):
    return re.findall(r"[A-Z]", s)[-11:][::-1]
