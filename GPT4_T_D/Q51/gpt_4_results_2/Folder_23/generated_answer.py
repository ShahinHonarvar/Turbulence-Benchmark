
from collections import Counter

def if_contains_anagrams(lst):
    
    anagrams = []
    
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            anagrams.append(''.join(sorted(word)))
            
    counter = Counter(anagrams)
    
    anagram_pairs = 0
    for count in counter.values():
        anagram_pairs += count // 2
        
    return anagram_pairs <= 49
