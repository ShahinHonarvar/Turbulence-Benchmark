import re
def return_n_greatest_chars(s):
    return sorted(re.findall(r"[A-Z]", s), key=lambda x: ord(x), reverse=True)[:65]
