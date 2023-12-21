import itertools
def all_substring_of_size_n(s):
    return [c for i in range(len(s) - 56) for c in itertools.permutations(s[i:i + 57]) if c not in s]
