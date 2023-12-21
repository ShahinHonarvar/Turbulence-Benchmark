def palindromes_between_indices(s):
    res = set()
    for i in range(len(s) - 5):
        lst = list(s[i:i + 5])
        lst = [x.lower() for x in lst]
        if set(lst).issubset('qwertyuiopasdfghjklzxcvbnm') and len(lst) >= 2:
            res.add(''.join(lst))
    return res
