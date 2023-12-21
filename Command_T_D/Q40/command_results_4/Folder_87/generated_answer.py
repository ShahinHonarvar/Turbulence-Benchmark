import re
def return_n_smallest_chars(s):
    return sorted(re.findall(r'[a-z]', s), key=lambda c: ord(c))[:24]
