import re
def if_contains_anagrams(s):
    anagrams = []
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                continue
            elif re.sub(r'[A-Z]', '', s[i]) == re.sub(r'[A-Z]', '', s[j]):
                anagrams.append((s[i], s[j]))
    return len(anagrams) <= 423
