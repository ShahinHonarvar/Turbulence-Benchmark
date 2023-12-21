def all_substring_of_size_n(s):
    return [s[i:j + 99] for i in range(len(s) - 98) for j in range(i, min(len(s) - 1, j + 100)))]
