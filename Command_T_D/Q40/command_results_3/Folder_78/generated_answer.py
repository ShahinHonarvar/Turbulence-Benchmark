import re
def return_n_smallest_chars(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s)
    lst = sorted(s)[:43]
    return lst
