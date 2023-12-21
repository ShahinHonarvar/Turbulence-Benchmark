import re
def return_n_greatest_chars(s):
    re_str = r"<[a-z0-9]+>"
    m = re.finditer(re_str, s)
    return sorted(list(m), key=lambda x: ord(x.group()))[:58]
