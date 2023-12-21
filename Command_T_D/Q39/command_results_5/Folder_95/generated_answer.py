import re
def return_n_greatest_chars(s):
    return sorted(re.findall(r'[A-Z0-9]+', s), key=lambda x: ord(x))[:36]
