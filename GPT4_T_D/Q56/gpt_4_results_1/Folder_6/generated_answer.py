
def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        if len(s[i:i+23]) == 23 and len(set(s[i:i+23])) == 23:
            if s[i:i+23] not in res:
                res.append(s[i:i+23])
    return res
