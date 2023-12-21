
def all_substring_of_size_n(s):
    res = []
    for i in range(0, len(s) - 51):
        substr = s[i:i + 52]
        if len(substr) == len(set(substr)):
            res.append(substr)
    return list(set(res))
