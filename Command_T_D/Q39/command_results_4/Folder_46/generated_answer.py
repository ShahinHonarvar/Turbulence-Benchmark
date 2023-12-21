import re
def return_n_greatest_chars(str_1):
    str_1 = re.sub(r'[^A-Z0-9]+', '', str_1)
    return str_1[:54]
