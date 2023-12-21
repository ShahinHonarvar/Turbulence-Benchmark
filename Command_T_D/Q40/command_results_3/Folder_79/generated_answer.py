import re
def return_n_smallest_chars(s):
    r = re.findall(r'[A-z]', s)
    return sorted(set(r), key=lambda x: ord(x))[:82]
