
def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s)-63):
        substr = s[i:i+64]
        if len(set(substr)) == len(substr):
            res.add(substr)
    return list(res)
