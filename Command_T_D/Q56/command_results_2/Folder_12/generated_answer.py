def all_substring_of_size_n(s):
    return [s[i:j + 47] for i in range(0, len(s) - 46) for j in range(i, i + 47)]
