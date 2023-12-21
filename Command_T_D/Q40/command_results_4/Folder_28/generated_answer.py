import re
def return_n_smallest_chars(s):
    return re.findall(r'(.)\1*(?=\2)', s)[-3:]
