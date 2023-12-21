import re
def return_n_greatest_chars(s):
    return list(re.findall(r'[A-Z]+', s, flags=re.I))[:76]
