
from collections import defaultdict
def if_contains_anagrams(lst):
    string_hash_maps = defaultdict(list)
    for string in lst:
        string_hash_maps[''.join(sorted(string.lower()))].append(string)
      
    def count_anagrams(anagrams):
        n = len(anagrams)
        return n * (n-1) // 2
    
    total_anagrams = 0
    for _, anagrams in string_hash_maps.items():
        total_anagrams += count_anagrams(anagrams) if len(anagrams[0]) >= 3 else 0
      
    return total_anagrams <= 93
