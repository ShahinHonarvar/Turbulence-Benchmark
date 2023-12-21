import re
def return_n_smallest_chars(s):
    s = re.sub(r'[^A-z]', '', s)
    return sorted(s)[-77:]
