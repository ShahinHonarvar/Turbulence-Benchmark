
def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 22):
        substr = s[i:i+23]
        if len(set(substr)) == len(substr):
            res.append(substr)
    return list(set(res))
