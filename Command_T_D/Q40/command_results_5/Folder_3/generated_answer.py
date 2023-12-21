import re
def return_n_smallest_chars(s):
    return sorted(re.findall("[a-z]", s), key=lambda c: ord(c))[:28]
