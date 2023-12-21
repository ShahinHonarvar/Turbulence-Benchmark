
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(list)
    for item in lst:
        item = item.lower()
        if len(item) >= 3:
            anagram_counts["".join(sorted(item))].append(item)
    anagram_pairs = sum(len(value)*(len(value)-1)/2 for value in anagram_counts.values())
    
    return anagram_pairs <= 25
