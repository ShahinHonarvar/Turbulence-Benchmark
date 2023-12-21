import re
def all_substring_of_size_n(s):
    if not s: return []
    m = re.fullmatch(r'(.)\1*', s)
    if m: return [m.group(1)]
    return []
