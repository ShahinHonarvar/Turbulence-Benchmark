import re
def return_n_greatest_chars(s):
    a = re.findall(r'[a-z]', s)
    b = re.findall(r'[A-Z]', s)
    c = re.findall(r'[0-9]', s)
    d = re.findall(r'[~!@#$%^-&*_+=<>?|}', s)
    m = a + b + c + d
    m.sort()
    return m[:29]
