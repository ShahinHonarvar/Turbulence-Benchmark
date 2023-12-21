import re
def return_n_smallest_chars(s):
    m = re.match(r'[A-Z]+', s)
    return m.group()[:58]
