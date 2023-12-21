import re
def all_substring_of_size_n(s):
    return re.findall(r'[A-z]{1,127}', s)
