
from collections import Counter

def if_contains_anagrams(lst):
    pairs_count = 0
    strings = [''.join(sorted(word.lower())) for word in lst if len(word)>=3]
    
    string_counts = Counter(strings)
    
    for count in string_counts.values():
        pairs_count += count*(count-1)//2
    
    return pairs_count <= 392
