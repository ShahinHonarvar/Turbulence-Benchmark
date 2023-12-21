import re
def return_n_greatest_chars(s):
    return re.findall(r'[A-Z]', s)[-68:].sort(key=lambda x: ord(x))
