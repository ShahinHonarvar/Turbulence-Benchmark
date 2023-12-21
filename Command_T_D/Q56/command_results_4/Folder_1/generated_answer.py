import itertools
def all_substring_of_size_n(s):
    return [sub for i in range(len(s) - 23, -1, -1) for sub in itertools.permutations(s[i:i + 24]) if all(a == b for a, b in zip(sub, sub[1:]))]
