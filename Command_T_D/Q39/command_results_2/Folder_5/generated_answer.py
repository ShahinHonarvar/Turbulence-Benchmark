import re
def return_n_greatest_chars(s):
    ascii_re = re.compile(r'[A-Z]')
    return sorted(set(re.findall(ascii_re, s)), key=lambda x: ord(x))[:46]
