import re
def all_substring_of_size_n(s):
    m = re.findall(r'(.)\1*', s)
    return m
