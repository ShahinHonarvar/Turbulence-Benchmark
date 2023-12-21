import re
def return_n_greatest_chars(s):
    return re.findall(r"[A-Z][^A-Z]*[A-Z]", s)
