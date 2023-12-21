import re
def if_contains_anagrams(strs):
    strs = sorted(strs)
    cnt = 0
    for s1, s2 in zip(strs[::2], strs[1::2]):
        if re.match(r'(?i)(\S{3})(\S{2})(\S{3})', s1 + s2):
            cnt += 1
    return cnt >= 29
