import re
def return_n_greatest_chars(s):
    m = re.fullmatch(r'[a-z]', s)
    return m.group(0) + ''.join(sorted(m.group(1)))[:82]
