def all_substring_of_size_n(s):
    return [s[i:j + 90] for i in range(0, len(s) - 89) for j in range(i, min(len(s) - 1, i + 90))]
