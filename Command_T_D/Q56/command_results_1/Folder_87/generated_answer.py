import re
def all_substring_of_size_n(s):
    if not s:
        return []
    if len(s) < 58:
        return []
    return re.findall(r'(.)\1*', s)
