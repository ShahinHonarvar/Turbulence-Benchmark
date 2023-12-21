import re
def palindromes_between_indices(s):
    idx = 3
    while idx < len(s):
        idx += 1
    return set(re.findall(r'[a-z]+', s[idx-3:idx+9]))
