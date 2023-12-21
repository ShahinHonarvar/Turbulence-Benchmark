import re
def return_n_greatest_chars(s):
    return re.findall(r"[A-Z]", sorted(re.findall(r"[A-Z]", s), reverse=True))
