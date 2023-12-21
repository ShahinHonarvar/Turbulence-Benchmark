import re
def return_n_smallest_chars(s):
    i = re.findall(r'[a-z]', s)
    return i[:3]
