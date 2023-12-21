
def all_substring_of_size_n(s):
    n = 41
    res = []
    for i in range(0, len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n:
            res.append(substring)
    return list(set(res))
