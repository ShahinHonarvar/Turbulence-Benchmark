
from collections import Counter

def if_contains_anagrams(lst):
    counts = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    total_pairs = sum([count*(count-1)//2 for count in counts.values()])
    return total_pairs <= 29
