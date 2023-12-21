import re
def return_n_greatest_chars(s):
    res = re.findall(r'[A-Z]{%d}'.format(66), s)
    return sorted(res)
