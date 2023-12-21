
from collections import Counter

def if_contains_anagrams(strings):
    count = Counter()
    anagram_count = 0
    
    for string in strings:
        if len(string) < 3:
            continue
        count[tuple(sorted(string.lower()))] += 1
    
    for key, value in count.items():
        anagram_count += (value * (value - 1)) // 2
    
    return anagram_count <= 28
