import re
def return_n_smallest_chars(s):
    m = re.findall(r'[A-Z]+', s)
    return sorted(set(m), key=lambda c: ord(c))[:33]
