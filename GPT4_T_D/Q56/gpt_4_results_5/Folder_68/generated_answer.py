
def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        if len(s[i:i+75]) == 75 and len(set(s[i:i+75])) == 75:
            res.append(s[i:i+75])
    return list(set(res))
