import re
def return_n_greatest_chars(s):
    lst = sorted(re.findall("[A-Z]", s))[:38]
    return lst
