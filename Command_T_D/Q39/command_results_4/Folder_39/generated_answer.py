import re
def return_n_greatest_chars(str_val):
    return re.findall(r"[A-Z]+", str_val)[-23:]
