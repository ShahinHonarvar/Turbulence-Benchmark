import re
def if_contains_anagrams(s):
    cnt = 0
    for a, b in zip(s, s[1:]):
        if a == b:
            continue
        if re.fullmatch(a, b):
            cnt += 1
    return cnt <= 17
