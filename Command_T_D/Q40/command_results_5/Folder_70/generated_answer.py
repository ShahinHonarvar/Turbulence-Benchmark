import re
def return_n_smallest_chars(s):
    return re.findall(r'(\w)', s)[-2]
