
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s, t):
        return Counter(s) == Counter(t)

    anagram_pairs = 0
    strngs = [s.lower() for s in lst if len(s)>=3]
    for i in range(len(strngs)):
        for j in range(i+1, len(strngs)):
            if is_anagram(strngs[i], strngs[j]):
                anagram_pairs += 1
                if anagram_pairs > 69:
                    return False
    return True
