def all_substring_of_size_n(s):
    return [s[i:i + 40] for i in range(len(s) - 39)]
