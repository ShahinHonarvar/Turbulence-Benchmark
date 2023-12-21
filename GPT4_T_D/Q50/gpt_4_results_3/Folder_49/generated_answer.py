
from collections import defaultdict

def if_contains_anagrams(strings):
    recorded_anagrams = defaultdict(set)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = "".join(sorted(string.lower()))
        recorded_anagrams[sorted_string].add(string.lower())
    
    count = 0
    for anagrams in recorded_anagrams.values():
        n = len(anagrams)
        if n > 1:
            count += n*(n-1)/2
        if count >= 59:
            return True
    return False
