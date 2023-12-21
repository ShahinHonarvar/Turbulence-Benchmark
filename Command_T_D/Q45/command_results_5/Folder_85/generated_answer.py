import re
def palindromes_between_indices(s):
    str_set = set(re.findall(r'[a-z]+', s[2:8]))
    return {s[i:j] for i in range(3, j, -1) for j in range(i+1, len(s), 1) if set(re.findall(r'[a-z]+', s[i:j])) <= str_set}
