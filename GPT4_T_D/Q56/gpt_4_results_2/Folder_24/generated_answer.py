
def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s)-51):
        substring = s[i:i+52]
        if len(set(substring)) == 52:
            res.add(substring)
    return list(res)
