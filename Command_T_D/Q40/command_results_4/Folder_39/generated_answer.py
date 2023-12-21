import re
def return_n_smallest_chars(s):
    re_list = re.findall(r'[a-z]', s)
    a = sorted(re_list)[:23]
    return a
