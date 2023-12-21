def all_substring_of_size_n(s):
    return [i for i in range(len(s) - 1, -1, -1) if all(c == s[j] for j, c in enumerate(i))]
