import re
def return_n_greatest_chars(s):
    res = re.findall(r'\w+', s)[-34:]
    return res
