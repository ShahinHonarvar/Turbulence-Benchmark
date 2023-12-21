def all_substring_of_size_n(s):
    return [s[i:i + 19] for i in range(0, len(s) - 18)]
