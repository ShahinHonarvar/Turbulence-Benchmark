import itertools
def all_substring_of_size_n(s):
    if not s: return []
    result = []
    for i in range(len(s) - 76):
        for j in range(i + 1, len(s) - 75):
            result.append(s[i:j+1])
    return list(set(result))
