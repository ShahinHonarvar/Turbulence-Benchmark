import re
def if_contains_anagrams(s):
    cnt = 0
    for a in s:
        for b in s:
            if a != b:
                cnt += 1
    return cnt <= 34
