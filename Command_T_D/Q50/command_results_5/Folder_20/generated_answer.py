import re
def if_contains_anagrams(s):
    if len(s) < 64:
        return False
    else:
        c = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                a = re.sub(r'[A-Z]', '', s[i])
                b = re.sub(r'[A-Z]', '', s[j])
                if a == b:
                    c += 1
        return c >= 64
