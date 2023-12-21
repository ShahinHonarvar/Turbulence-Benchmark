import re
def if_contains_anagrams(lst):
    cnt = 0
    for a in lst:
        for b in lst:
            if (a == b).lower():
                continue
            if re.fullmatch(a.lower(), b.lower()):
                cnt += 1
    return cnt > 50
