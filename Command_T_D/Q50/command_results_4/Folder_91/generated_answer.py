def if_contains_anagrams(lst):
    res = 0
    for s in lst:
        temp = 0
        for i in range(len(s) - 2):
            if s[i] != s[i + 1]:
                temp += 1
        if temp >= 6:
            res += 1
    return res >= 6
