import re
def if_contains_anagrams(s):
    anagrams = set()
    for i in range(len(s)):
        s[i] = s[i].lower()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if re.match(r'(.*?)\1', s[i], re.I):
                anagrams.add(s[i])
                anagrams.add(s[j])
    return len(anagrams) >= 94
