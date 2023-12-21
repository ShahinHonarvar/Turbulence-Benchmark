import re
def return_n_smallest_chars(s):
    m = re.findall("[a-z]", s)
    return sorted(m[:5])
