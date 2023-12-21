import re
def return_n_greatest_chars(s):
    s = re.sub(r'[^A-Z0-9]+', '', s)
    s = sorted(s)[:89]
    return s
