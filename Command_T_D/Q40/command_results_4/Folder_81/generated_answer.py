import re
def return_n_smallest_chars(s):
    m = re.match(r'([a-z]+)', s)
    return sorted(m.group())[:64]
