import re
def return_n_smallest_chars(s):
    r = re.findall(r'[a-z]', s)
    return sorted(r, key=lambda i: ord(i))[:63]
