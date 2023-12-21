import itertools
def all_substring_of_size_n(s):
    return [ sub for i in range(len(s)) for sub in itertools.permutations(s[i:], len(s[i:])) if len(set(sub)) == 26 ]
