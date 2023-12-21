import re
def all_substring_of_size_n(s):
    res = re.findall(r'([\d]+)', s)
    return res
