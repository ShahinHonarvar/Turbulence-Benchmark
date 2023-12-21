
import collections

def if_contains_anagrams(lst):
    anagram_count = 0
    counter = collections.Counter()
    
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            counter[word_lower] += 1
    
    for count in counter.values():
        anagram_count += count * (count - 1) / 2
    
    if anagram_count <= 94:
        return True
    else:
        return False
