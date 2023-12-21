
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    anagram_counter = 0
    formats = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    for pair in combinations(formats, 2):
        if pair[0] == pair[1]:
            anagram_counter += 1
    
    if anagram_counter <= 61:
        return True
    else:
        return False
