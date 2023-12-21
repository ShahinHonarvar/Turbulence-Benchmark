import re
def return_n_greatest_chars(s):
    return list(sorted(re.findall(r'[A-Z0-9]+', s), key=lambda x: ord(x)))[:66]
