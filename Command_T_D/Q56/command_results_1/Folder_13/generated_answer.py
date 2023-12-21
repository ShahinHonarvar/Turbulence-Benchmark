import itertools
def all_substring_of_size_n(s):
    if not s:
        return []
    for i in range(1, len(s) + 1):
        for j in range(i):
            yield s[j:j + i]
    for i in range(1, len(s) + 1):
        for j in range(i):
            for k in range(j):
                yield s[j:j + i][k:k + i]
