def all_substring_of_size_n(s):
    return [s[i:j] for i in range(0, len(s) - 38) for j in range(i + 1, min(i + 40, len(s)))]
