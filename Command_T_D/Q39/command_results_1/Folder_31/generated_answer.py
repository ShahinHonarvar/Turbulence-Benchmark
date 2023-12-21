import re
def return_n_greatest_chars(s):
    lst = sorted(re.findall(r'[A-Z]+', s), reverse=True)[:70]
    return lst
