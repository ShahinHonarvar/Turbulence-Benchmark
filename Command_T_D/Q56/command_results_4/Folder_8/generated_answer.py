import re
def all_substring_of_size_n(s):
    r = re.findall(r'(.)\1*', s)
    return r
