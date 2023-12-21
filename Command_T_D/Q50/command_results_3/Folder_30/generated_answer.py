def if_contains_anagrams(s):
    cnt = 0
    for x in s:
        y = str(x).lower()
        if len(y) >= 3:
            if y in y:
                cnt += 1
    return cnt >= 78
