
from collections import Counter

def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())

    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs >= 246:
                    return True
    return False
