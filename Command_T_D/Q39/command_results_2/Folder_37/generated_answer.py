import re
def return_n_greatest_chars(s):
    m = re.findall(r'[A-Z]', s)
    m.sort(key=lambda c: ord(c))
    return m[:26]
