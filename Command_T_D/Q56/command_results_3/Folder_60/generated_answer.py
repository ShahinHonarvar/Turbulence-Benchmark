import re
def all_substring_of_size_n(s):
    return re.findall(r'.{36}', s)
