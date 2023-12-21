import re
def if_contains_anagrams(s):
    for j in range(len(s)):
        for k in range(j + 1, len(s)):
            if re.match(r'[a-z]+', s[j].lower() + s[k].lower()):
                continue
            else:
                return False
    return True
