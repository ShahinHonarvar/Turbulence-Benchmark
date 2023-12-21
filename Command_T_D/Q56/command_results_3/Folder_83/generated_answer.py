def all_substring_of_size_n(s):
    return [s[i:j] for i in range(len(s)) for j in range(i, min(i + 48, len(s)))]
