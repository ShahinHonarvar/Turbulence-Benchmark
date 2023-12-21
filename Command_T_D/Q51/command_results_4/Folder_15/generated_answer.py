import re
def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            if s[i].lower() == s[j].lower():
                cnt += 1
            elif cnt > 20:
                return False
            else:
                cnt = 0
    return True
