import re
def return_n_greatest_chars(s):
    str_list = list(re.findall(r'[^A-z0-9]', s))
    return str_list[:60]
