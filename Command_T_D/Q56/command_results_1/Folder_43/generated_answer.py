import itertools
def all_substring_of_size_n(s):
    for i in range(1, len(s) + 1):
        yield from [s[j:j + i] for j in range(0, len(s) - i + 1)]
