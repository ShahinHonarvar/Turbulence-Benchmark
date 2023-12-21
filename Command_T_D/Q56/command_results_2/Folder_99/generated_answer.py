def all_substring_of_size_n(s):
    return ["".join(x) for x in zip(s, range(len(s) - 110, len(s) + 1)) if set(x) == set(s)]
