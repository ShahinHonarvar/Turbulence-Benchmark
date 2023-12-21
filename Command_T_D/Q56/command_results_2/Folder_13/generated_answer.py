def all_substring_of_size_n(s):
    return [c for c in set(s[i:j+53] for i in range(0, len(s) - 52)) if c]
