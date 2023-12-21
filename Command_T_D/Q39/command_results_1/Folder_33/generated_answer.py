import re
def return_n_greatest_chars(s):
    x = list(sorted(re.findall(r"[A-Z]", s)))[:36]
    return x
