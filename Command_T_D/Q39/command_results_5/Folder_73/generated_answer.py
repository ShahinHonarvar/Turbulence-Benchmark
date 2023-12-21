import re
def return_n_greatest_chars(s):
    s += '\0'
    return sorted(re.findall('\w+', s)[-80:])
