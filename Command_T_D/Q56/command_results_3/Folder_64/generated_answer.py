def all_substring_of_size_n(s):
    return [i for i in range(len(s) - 7, -1, -1) if s[i:i + 8] not in s[i:]]
