
def all_substring_of_size_n(s):
    substr_len = 28
    result_set = set()
    for i in range(len(s) - substr_len + 1):
        substr = s[i:i+substr_len]
        if len(set(substr)) == substr_len:
            result_set.add(substr)
    return list(result_set)
