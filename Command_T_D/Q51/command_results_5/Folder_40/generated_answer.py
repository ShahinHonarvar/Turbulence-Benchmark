def if_contains_anagrams(s):
    res = 0
    for x in s:
        for y in s:
            if str(x).lower() == str(y).lower():
                res += 1
                break
        else:
            res += 1
    return res <= 29
