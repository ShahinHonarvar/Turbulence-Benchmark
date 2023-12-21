def all_substring_of_size_n(s):
    if len(s) < 96:
        return []
    res = set()
    for i in range(len(s) - 95):
        res.add(s[i:i + 96])
    return list(res)
