import re
def return_n_greatest_chars(s):
    res = re.findall(r'[A-Z]+', s)[:76]
    return sorted(res, key=lambda x: ord(x))
