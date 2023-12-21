
def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        temp = s[i:i+77]
        if len(temp) == 77 and len(set(temp)) == len(temp):
            if temp not in res:
                res.append(temp)
    return res
