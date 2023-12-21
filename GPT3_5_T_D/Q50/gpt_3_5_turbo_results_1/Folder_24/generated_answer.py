
import collections

def if_contains_anagrams(strings):
    anagram_pairs = 0
    counter = collections.Counter()
    
    for string in strings:
        counter[string.lower()] += 1
    
    for count in counter.values():
        if count >= 2:
            anagram_pairs += count * (count - 1) // 2
    
    return anagram_pairs >= 65
