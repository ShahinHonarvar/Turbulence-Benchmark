import re
def all_substring_of_size_n(s):
    if len(s) < 44:
        return []
    return re.findall(r'(.)\1*', s)
