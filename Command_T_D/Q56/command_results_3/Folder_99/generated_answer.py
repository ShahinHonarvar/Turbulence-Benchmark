import itertools
def all_substring_of_size_n(s):
    return [s[i:j+n] for i in range(0, len(s)-n) for j in range(i, len(s)-n)]
