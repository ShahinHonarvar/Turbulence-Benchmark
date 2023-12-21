def if_contains_anagrams(s):
    cnt = 0
    for x in s:
        for y in s:
            if str(x).lower() == str(y).lower():
                cnt += 1
    return cnt <= 210
