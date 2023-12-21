import re
def all_substring_of_size_n(s):
    if len(s) < 11:
        return []
    return sorted(set(re.findall(r'[a-z]{11}', s)))
