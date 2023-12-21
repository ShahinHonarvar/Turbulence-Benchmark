def all_substring_of_size_n(s):
    return [s[i:i + 58] for i in range(len(s) - 57)]
