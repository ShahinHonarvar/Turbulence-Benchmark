def all_substring_of_size_n(s):
    return [sub for i in range(26) for sub in s[i:i + 26]]
