
from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = 0
    count = Counter([''.join(sorted(string.lower())) for string in string_list if len(string) >= 3])
    for c in count.values():
        anagrams += c * (c - 1) // 2
    
    return anagrams >= 43
