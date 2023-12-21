import re
def return_n_greatest_chars(s):
    s = list(re.findall("[A-Z0-9]", s))
    s.sort(key=lambda x: ord(x))
    return s[:72]
