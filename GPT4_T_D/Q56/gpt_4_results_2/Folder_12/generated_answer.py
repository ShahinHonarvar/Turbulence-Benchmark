
def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        if i + 47 <= len(s):
            substring = s[i: i + 47]
            if len(set(substring)) == len(substring):
                res.append(substring)
    return list(set(res))
