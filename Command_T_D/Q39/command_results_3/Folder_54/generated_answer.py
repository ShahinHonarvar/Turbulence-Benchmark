import re
def return_n_greatest_chars(str_val):
    str_val = re.sub(r'[^A-Z0-9]+', '', str_val)
    return str_val[:79].split()
