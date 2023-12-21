import re
def return_n_greatest_chars(s):
    m = re.findall(r'[A-Z]', s)
    m.sort()
    return m[:2]
