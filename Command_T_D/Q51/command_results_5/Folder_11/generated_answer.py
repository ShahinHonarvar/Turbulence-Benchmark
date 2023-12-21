import re
def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s) - 2):
        cnt += s[i:i + 2] == s[i:i + 2].lower()
    return cnt <= 41
