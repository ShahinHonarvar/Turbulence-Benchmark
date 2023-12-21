def all_substring_of_size_n(s):
    return ["".join(c for c in s if c) for i in range(len(s) + 1)]
