
def all_substring_of_size_n(s):
    res = []
    n = 69
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == len(substr):
            res.append(substr)
    return list(set(res))
