
def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        if i+95 > len(s):
            break 
        ss = s[i:i+95]
        if len(set(ss)) == 95:
            if ss not in res:
                res.append(ss)
    return res
