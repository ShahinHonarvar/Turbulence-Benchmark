import re
def return_n_smallest_chars(s):
    r = re.findall(r'[a-z]', s)
    r.sort()
    return r[:35]
