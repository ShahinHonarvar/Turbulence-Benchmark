
from collections import defaultdict

def if_contains_anagrams(lst):
    counter = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter[sorted_word] += 1

    pairs = sum(1 for count in counter.values() if count > 1)
    
    return pairs >= 8
