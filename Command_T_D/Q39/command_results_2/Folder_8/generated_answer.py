import re
def return_n_greatest_chars(str_):
    s = re.sub(r'[^A-z0-9]+', '', str_)
    return sorted(set(s), key=lambda x: ord(x))[:83]
