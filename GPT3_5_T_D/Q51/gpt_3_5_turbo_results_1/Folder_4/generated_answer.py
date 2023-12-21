
from itertools import combinations
from collections import Counter

def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())
    
    count = 0
    for word1, word2 in combinations(strings, 2):
        if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
            count += 1
            if count > 84:
                return False
    
    return True
