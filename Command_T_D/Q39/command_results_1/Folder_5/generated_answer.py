import re
def return_n_greatest_chars(s):
    a = re.findall(r"[A-Z]", s)
    a.sort(reverse=True)
    a = a[:46]
    return a
