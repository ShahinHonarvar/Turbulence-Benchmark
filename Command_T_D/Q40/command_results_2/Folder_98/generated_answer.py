import re
def return_n_smallest_chars(s):
    return sorted(re.findall("[A-Z0-9]", s), key=lambda x: ord(x))[:68]
