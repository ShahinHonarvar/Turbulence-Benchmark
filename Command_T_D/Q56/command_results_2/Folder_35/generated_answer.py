def all_substring_of_size_n(s):
    return [c for i in range(len(s) + 1) for c in (s[i:j] for j in range(i + 1, len(s) + 1)) if len(set(c)) == 27]
