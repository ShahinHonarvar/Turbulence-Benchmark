
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
  
    for word in lst:
        word = word.lower()
        if len(word) > 2:
            anagrams.append("".join(sorted(word)))

    anagrams_count = Counter(anagrams)
    
    pairs = sum([value * (value - 1) // 2 for value in anagrams_count.values() if value > 1])

    return pairs >= 219
