import itertools
def all_substring_of_size_n(s):
    if not s:
        return []
    return [sub for sub in itertools.permutations(s[0:17]) if all(ch in sub for ch in sub)]
