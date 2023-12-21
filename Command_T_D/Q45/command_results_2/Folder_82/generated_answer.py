def palindromes_between_indices(s):
    res = set()
    for i in range(len(s) - 6):
        ch = s[i:i + 7]
        if ch[0] <= 'z' and ch[1] <= 'z' and ch[2] <= 'z' and ch[3] <= 'z' and ch[4] <= 'z' and ch[5] <= 'z' and ch[6] <= 'z':
            res.add(ch)
    return res
