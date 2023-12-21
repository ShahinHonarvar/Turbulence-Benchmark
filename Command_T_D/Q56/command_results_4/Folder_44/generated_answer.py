def all_substring_of_size_n(s):
    return [w for w in s[i:i + 90] for i in range(0, len(s) - 89)]
