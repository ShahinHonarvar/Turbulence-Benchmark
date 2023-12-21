import re
def return_n_smallest_chars(s):
    m = re.findall(r'[a-z]', s)
    m.sort()
    return m[:79]
