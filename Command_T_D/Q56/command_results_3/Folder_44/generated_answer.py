def all_substring_of_size_n(s):
    if len(s) < 90:
        return []
    return [s[i:j] for i in range(len(s)) for j in range(i, min(len(s), i + 90))]
