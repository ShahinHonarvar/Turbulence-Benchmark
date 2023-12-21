import itertools
def all_substring_of_size_n(s):
    if len(s) < 18:
        return []
    s += '*' * 18
    return [s[i:j+1] for i in range(0, len(s)-17) for j in range(i, len(s)-16)]
