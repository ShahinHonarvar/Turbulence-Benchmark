import re
def all_substring_of_size_n(s):
    if not s:
        return []
    res = []
    for i in range(1, len(s) + 1):
        res += [s[:i]]
    return list(set(res))
