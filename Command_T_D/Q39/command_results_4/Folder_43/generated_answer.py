import re
def return_n_greatest_chars(s):
    return re.findall(r"<[a-z]", s)[::-1][0:56]
