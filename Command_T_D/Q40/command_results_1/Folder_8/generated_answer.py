import re
def return_n_smallest_chars(s):
    return sorted(re.findall(r'[A-Z]', s))[:83]
