
from collections import Counter

def if_contains_anagrams(string_list):
    words = [''.join(sorted(w)) for w in string_list if len(w)>=3]
    counts = Counter(words)
    anagrams = [val for val in counts.values() if val > 1]
    pairs = sum([val*(val-1)//2 for val in anagrams])
    return pairs <= 277
