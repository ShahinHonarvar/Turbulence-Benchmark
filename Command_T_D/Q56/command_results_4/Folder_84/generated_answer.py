def all_substring_of_size_n(s):
    if not s:
        return []
    res = []
    i = j = 0
    while j < len(s):
        res.append(s[i:j])
        i += 1
        j += 114
    return res
