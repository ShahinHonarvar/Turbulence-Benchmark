def all_substring_of_size_n(s):
    return [sub for i in range(len(s) - 126) for sub in s[i:i + 127]]
