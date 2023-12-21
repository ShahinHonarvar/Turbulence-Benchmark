import re
def return_n_smallest_chars(s):
    return sorted(re.findall(r'[a-z]', s), key=lambda x: ord(x))[:64]
