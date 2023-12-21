import re
def if_contains_anagrams(s):
    if len(s) >= 3:
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if re.match(r'[a-z]+', s[i].lower()) == re.match(r'[a-z]+', s[j].lower()):
                    return True
    return False
