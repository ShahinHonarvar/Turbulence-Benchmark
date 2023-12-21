
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())
    
    pairs = list(combinations(lst, 2))
    anagram_pairs = [pair for pair in pairs if len(pair[0])>2 and len(pair[1])>2 and is_anagram(pair[0], pair[1])]
    return len(anagram_pairs) <= 318
