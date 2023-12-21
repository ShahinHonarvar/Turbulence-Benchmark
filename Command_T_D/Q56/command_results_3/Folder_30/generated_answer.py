def all_substring_of_size_n(s):
    return ["".join(sorted(s[i:j + 1])) for i in range(0, len(s) - 78)]
