def all_substring_of_size_n(s):
    return [i for i in range(len(s) - 19, -1, -1) if s[i:i + 20] not in s[:i] + s[i + 20:]]
