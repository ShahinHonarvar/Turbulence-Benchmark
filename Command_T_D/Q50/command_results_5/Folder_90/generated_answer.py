import re
def if_contains_anagrams(lst):
    cnt = 0
    for s in lst:
        cnt += sum(1 for i in range(len(s)) if re.sub(r"[A-Z]", "", s[:i] + s[i+1:]))
    return cnt >= 177
