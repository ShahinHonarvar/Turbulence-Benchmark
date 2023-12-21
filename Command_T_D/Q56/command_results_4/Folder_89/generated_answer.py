import re
def all_substring_of_size_n(s):
    if not s:
        return []
    return sorted(set(re.findall(r'(.)\1*', s)))
