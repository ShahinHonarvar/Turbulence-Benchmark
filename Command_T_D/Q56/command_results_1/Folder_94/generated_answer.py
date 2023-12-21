import re
def all_substring_of_size_n(s):
    return re.findall(r'[a-zA-Z0-9]+', s, flags=re.I)
