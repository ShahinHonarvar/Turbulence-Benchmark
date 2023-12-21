import re
def if_contains_anagrams(lst):
    cnt = 0
    for s in lst:
        for m in re.finditer(r'((?i)([a-z]{3}){2})', s):
            cnt += 1
    return cnt >= 43
