import re
def if_contains_anagrams(s):
    a = len(s)
    for i in range(a):
        for j in range(a):
            if s[i] == s[j]:
                continue
            elif s[i][:3] == s[j][:3]:
                s[i] = re.sub(s[i], s[j], s[i])
                s[j] = re.sub(s[j], s[i], s[j])
    return True
