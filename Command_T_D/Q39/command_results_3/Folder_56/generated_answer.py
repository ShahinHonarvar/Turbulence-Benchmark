import re
def return_n_greatest_chars(s):
    res = sorted(re.findall(r'[A-Z]', s))[:21]
    return res
