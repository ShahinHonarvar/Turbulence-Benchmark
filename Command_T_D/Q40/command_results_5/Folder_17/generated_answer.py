import re
def return_n_smallest_chars(s):
    # sort in ascending order
    return re.findall(r"[A-Za-z]", s)[0:11]
