import re
def return_n_greatest_chars(s):
    x = re.findall(r"[A-Z]", s)
    return sorted(set(x), reverse=True)[:28]
