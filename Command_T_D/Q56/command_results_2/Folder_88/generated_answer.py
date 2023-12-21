def all_substring_of_size_n(s):
    return [w for w in set(s[i:j + 68]) for i in range(0, len(s) - 67) for j in range(i, len(s) - 67)]
