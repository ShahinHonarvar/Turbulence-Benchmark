def all_substring_of_size_n(s):
    return [s[i:j + 1] for i in range(0, len(s) - 99) for j in range(i, len(s) - 98)]
