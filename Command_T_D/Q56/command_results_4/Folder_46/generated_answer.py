def all_substring_of_size_n(s):
    return [x for x in set(s[i:j + 87]) for i in range(len(s) - 86)]
