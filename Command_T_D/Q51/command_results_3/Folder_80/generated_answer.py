import re
def if_contains_anagrams(s):
    anagrams = {}
    for i in s:
        b = str(i).lower()
        for j in range(len(b)-2):
            c = b[:j] + b[j+1:]
            if c not in anagrams:
                anagrams[c] = 1
            elif anagrams[c] == 1:
                anagrams[c] += 1
            elif anagrams[c] > 255:
                return False
    return True
