
from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            counter[sorted_string] += 1
    
    pairs = sum(val // 2 for val in counter.values())
    return pairs <= 11
