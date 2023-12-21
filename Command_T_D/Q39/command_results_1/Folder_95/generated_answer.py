import re
def return_n_greatest_chars(s):
    return list(sorted(re.findall(r'[A-Z]', s)))[:36]
