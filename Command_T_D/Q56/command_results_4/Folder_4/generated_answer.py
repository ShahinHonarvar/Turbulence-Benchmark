import itertools
def all_substring_of_size_n(s):
    if not s:
        return []
    i = 0
    while i < len(s) - 40:
        yield ''.join(a for a in itertools.permutations(s[i:i+41]))
        i += 1
