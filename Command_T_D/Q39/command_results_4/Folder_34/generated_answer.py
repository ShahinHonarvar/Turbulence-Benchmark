import re
def return_n_greatest_chars(s):
    s = re.sub(r'[^A-Z]', '', s)
    s = sorted(s, reverse=True)[:9]
    return s
