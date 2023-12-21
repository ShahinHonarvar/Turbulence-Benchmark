
from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    anagram_counts = [val for val in counter.values() if val > 1]
    pairs = sum([val*(val-1)//2 for val in anagram_counts])
    return pairs >= 79
