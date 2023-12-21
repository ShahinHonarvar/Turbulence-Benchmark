
def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s)):
        if i + 69 <= len(s) and len(set(s[i:i+69])) == 69:
            res.add(s[i:i+69])
    return list(res)
