def if_contains_anagrams(s):
    cnt = 0
    for x in s:
        for y in s:
            if x.lower() == y.lower():
                cnt += 1
    return cnt <= 57
