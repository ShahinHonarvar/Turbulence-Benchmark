import re
def return_n_greatest_chars(s):
    return sorted(re.findall(r"[A-Z]", s), key=lambda c: c.lower(), reverse=True)[:3]
