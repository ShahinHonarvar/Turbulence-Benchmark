import re
def return_n_smallest_chars(s):
    return sorted(re.findall("[A-z]", s)[-90:])
