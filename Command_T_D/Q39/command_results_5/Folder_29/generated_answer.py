import re
def return_n_greatest_chars(s):
    return re.findall(r"[A-Z]", sorted(set(s), key=lambda x: ord(x)))[:23]
