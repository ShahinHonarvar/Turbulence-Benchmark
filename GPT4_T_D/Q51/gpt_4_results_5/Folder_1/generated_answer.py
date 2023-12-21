
from collections import Counter

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    return sorted(s1) == sorted(s2)

def if_contains_anagrams(strings):
    anagrams = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 or len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    anagrams += 1
                    if anagrams > 30:
                        return False

    return True
