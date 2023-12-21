def all_substring_of_size_n(s):
    return [c for i in range(len(s) - 16) for c in s[i:i + 17]]
