
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())
    
    pairs = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs >= 93:
                    return True
    return False
