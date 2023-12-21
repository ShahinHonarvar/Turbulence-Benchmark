def all_substring_of_size_n(s):
    return [c for c in s if len(c) == 6 and c not in s[1:]]
