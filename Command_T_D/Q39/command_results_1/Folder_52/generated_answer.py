import re
def return_n_greatest_chars(str1):
    res = re.findall(r"[A-Z]", str1)[:68]
    return res
