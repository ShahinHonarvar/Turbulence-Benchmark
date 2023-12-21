import re
def return_n_smallest_chars(s):
    m = re.findall(r'[A-Z]+', s)
    m.sort()
    return m[:39]
