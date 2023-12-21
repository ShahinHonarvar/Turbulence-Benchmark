
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counts = Counter()
    
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_counts[sorted_word] += 1
            
    num_pairs = sum(count // 2 for count in anagram_counts.values())

    return num_pairs >= 46
