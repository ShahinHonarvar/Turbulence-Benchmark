
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        key = "".join(sorted(word.lower()))
        if len(key) >= 3:
            anagrams[key].append(word)
            
    pairs = sum([len(value) // 2 for value in anagrams.values()])
    
    return pairs <= 5
