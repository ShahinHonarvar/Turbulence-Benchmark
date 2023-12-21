import re
def return_n_greatest_chars(s):
    n = 59
    return list(re.findall(r'[A-Z]', s)[::-1][:n])
