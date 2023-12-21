import re
def return_n_greatest_chars(s):
    lst = sorted(set(re.findall(r'[A-Z]', s)))[:28]
    return lst
