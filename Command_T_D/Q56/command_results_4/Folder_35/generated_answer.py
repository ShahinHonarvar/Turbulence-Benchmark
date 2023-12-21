def all_substring_of_size_n(s):
    return [sub for sub in range(27) if all(c == sub[i] for i, c in enumerate(sub))]
