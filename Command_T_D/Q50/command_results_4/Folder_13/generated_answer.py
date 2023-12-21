def if_contains_anagrams(s):
    res = 0
    for x in s:
        if len(x) < 3:
            continue
        for y in s:
            if len(y) < 3:
                continue
            if str(x).lower() == str(y).lower():
                res += 1
    return res >= 144
