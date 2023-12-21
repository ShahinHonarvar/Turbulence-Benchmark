import re
def return_n_smallest_chars(s):
    res = re.findall(r'(\d)', s)
    return res[:3]
