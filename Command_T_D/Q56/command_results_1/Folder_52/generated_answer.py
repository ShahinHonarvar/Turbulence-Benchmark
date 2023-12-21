def all_substring_of_size_n(s):
    return [s[i:j + 1] for i in range(len(s) - 14) for j in range(i, len(s) - 14)]
