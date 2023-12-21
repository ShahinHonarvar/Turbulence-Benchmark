
from collections import Counter
import itertools

def if_contains_anagrams(string_list):
    anagram_count = 0
    string_list = [''.join(sorted(n.lower())) for n in string_list if len(n) >= 3]
    
    counter = Counter(string_list)
    
    for value in counter.values():
        anagram_count += sum([num for num in range(value)])
        
    if anagram_count <= 173:
        return True
    else:
        return False
