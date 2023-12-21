import re
def if_contains_anagrams(list_str):
    res = 0
    for s in list_str:
        for i in range(len(s) - 2):
            if re.search(s[i:i+3], s[i+1:i+4], flags=re.I):
                res += 1
    return res >= 24
