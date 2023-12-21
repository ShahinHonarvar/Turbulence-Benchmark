def all_substring_of_size_n(s):
    return [[c for c in s[i:i + n]] for i in range(0, len(s) - 33) for n in range(1, 35)]
