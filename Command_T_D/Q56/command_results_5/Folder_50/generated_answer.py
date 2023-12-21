def all_substring_of_size_n(s):
    return [w for w in set(s[i:i + 11]) if len(w) == 11]
