import re
def return_n_greatest_chars(s):
    res = sorted(re.findall(r'[A-Z]', s), key=lambda x: ord(x))[:49]
    return res
