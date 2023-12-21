import re
def return_n_greatest_chars(s):
    m = re.findall(r'[A-Z]+', s)[:90]
    return sorted(set(m))
