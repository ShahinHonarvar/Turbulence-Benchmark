import re
def if_contains_anagrams(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if re.search(r'(?i)(?=.*\1)', s[i], re.I) and re.search(r'(?i)(?=.*\1)', s[j], re.I):
                return True
    return False
