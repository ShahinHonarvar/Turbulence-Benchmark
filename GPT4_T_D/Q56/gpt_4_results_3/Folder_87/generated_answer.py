
def all_substring_of_size_n(s):
    res = []
    for i in range(0, len(s)-57):
        substring = s[i:i+58]
        if len(set(substring)) == 58:
            res.append(substring)
    return list(set(res))
