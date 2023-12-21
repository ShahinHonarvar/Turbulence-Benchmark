import re
def return_n_smallest_chars(s):
    r = re.findall("[a-z]", s)
    return sorted(r)[-47:]
