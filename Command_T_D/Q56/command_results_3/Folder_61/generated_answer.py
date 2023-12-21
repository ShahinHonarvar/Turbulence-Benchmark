def all_substring_of_size_n(s):
    return [c for c in s[i:i + 39] for i in range(0, len(s) - 38)]
