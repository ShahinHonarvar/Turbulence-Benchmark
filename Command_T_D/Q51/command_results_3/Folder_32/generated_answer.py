import re
def if_contains_anagrams(text):
    anagrams = 0
    for s in text:
        s = s.lower()
        for i in range(len(s)-2):
            s1 = s[:i] + s[i+1:]
            s2 = s[i:] + s[:i]
            if s1 == s2:
                anagrams += 1
    return anagrams <= 89
