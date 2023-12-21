import re
def return_n_smallest_chars(s):
    m = re.findall("[A-Z0-9]+", s)
    return m[:49]
