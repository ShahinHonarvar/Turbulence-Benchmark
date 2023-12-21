import re
def if_contains_anagrams(s):
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s)):
            if (re.sub(r'[A-Z]+', '', s[i]) == re.sub(r'[A-Z]+', '', s[j])):
                return False
    return True
