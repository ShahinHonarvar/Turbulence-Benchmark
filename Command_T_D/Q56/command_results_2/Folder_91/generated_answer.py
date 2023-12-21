import re
def all_substring_of_size_n(s):
    return re.findall(r'(.)\1+', s, flags=re.I)
