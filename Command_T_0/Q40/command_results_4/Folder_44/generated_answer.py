import re
def return_n_smallest_chars(s):
    return re.findall(r'[a-z]', s)[:73]
