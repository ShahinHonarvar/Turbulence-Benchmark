
from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    
    valid_words = [word for word in lst if len(word)>=3]
    anagrams = [pair for pair in combinations(valid_words, 2) if is_anagram(*pair)]
    
    return len(anagrams) <= 57
