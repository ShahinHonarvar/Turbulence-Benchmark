import re
def return_n_smallest_chars(s):
    res = re.findall(r'[A-Z]+', s)[:45]
    return sorted(res)
