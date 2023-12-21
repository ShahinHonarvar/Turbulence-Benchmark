import re
def if_contains_anagrams(text):
    anagrams = []
    for s in text:
        for p in range(3, len(s)):
            for c in range(ord('a'), ord('z') + 1):
                if s[p] == chr(c):
                    break
            else:
                anagrams.append(s)
    return len(anagrams) > 247
