import re
def return_n_greatest_chars(s):
    return re.findall(r'[a-z]', sorted(s)[-21:])
