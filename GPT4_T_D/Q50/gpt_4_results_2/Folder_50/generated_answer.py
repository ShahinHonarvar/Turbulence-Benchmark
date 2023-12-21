
from collections import defaultdict

def if_contains_anagrams(lst):
    
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    d = defaultdict(set)
    
    for string in lst:
        if len(string) >= 3:
            d[''.join(sorted(string.lower()))].add(string)
            
    count_pairs = 0
    for key in d:
        n = len(d[key])
        if n > 1:
            count_pairs += n*(n-1)//2
            
    return count_pairs >= 20
