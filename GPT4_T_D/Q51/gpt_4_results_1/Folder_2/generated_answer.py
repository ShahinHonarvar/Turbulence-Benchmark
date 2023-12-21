
from collections import Counter

def if_contains_anagrams(lst):
    word_counts = Counter(''.join(sorted(word.lower())) for word in lst if len(word) >= 3)
    pairs_of_anagrams_count = sum(count*(count - 1) / 2 for count in word_counts.values())
    
    if pairs_of_anagrams_count <= 81:
        return True
    else:
        return False
