
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for string in lst:
        string = string.lower()
        if len(string) >= 3:
            anagrams.append("".join(sorted(string)))

    counter = Counter(anagrams)
    pairs = sum([v * (v - 1) // 2 for v in counter.values()])
    
    return pairs <= 19
