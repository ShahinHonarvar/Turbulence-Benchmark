def all_substring_of_size_n(s):
    return [x for x in set(s[i:j] for i in range(len(s)-10)) if len(set(x)) == 10]
