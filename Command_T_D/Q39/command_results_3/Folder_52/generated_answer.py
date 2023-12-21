import re
def return_n_greatest_chars(s):
    m = re.findall(r'[A-Z]{%68}', s)
    return m
