import re
def return_n_greatest_chars(s):
    result = re.findall(r"[A-Z]", s)[:44]
    return result
