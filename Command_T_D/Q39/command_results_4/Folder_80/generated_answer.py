import re
def return_n_greatest_chars(s):
    ascii_values = list(map(ord, s))
    ascii_values.sort()
    return re.findall(r'[A-Z]+', s)[-35:]
