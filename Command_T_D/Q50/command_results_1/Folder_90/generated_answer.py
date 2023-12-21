def if_contains_anagrams(s):
    res = False
    for x in s:
        for y in s:
            if str(x).lower() == str(y).lower():
                res = True
    return res
