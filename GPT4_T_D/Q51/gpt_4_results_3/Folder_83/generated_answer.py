
from collections import defaultdict

def if_contains_anagrams(lst):
    
    def is_anagram(s, t):
        return sorted(s) == sorted(t)
    
    def are_anagrams(lst):
        pairs = []
        for i in range(len(lst) - 1):
            for j in range(i+1, len(lst)):
                if is_anagram(lst[i], lst[j]) and (lst[i], lst[j]) not in pairs and (lst[j], lst[i]) not in pairs:
                    pairs.append((lst[i], lst[j]))
        return pairs
        
    lst = [x.lower() for x in lst]
    anagram_pairs = are_anagrams(lst)
    anagram_pairs = [pair for pair in anagram_pairs if len(pair[0]) >= 3 and len(pair[1]) >= 3]  
                  
    if len(anagram_pairs) <= 19:
        return True
    else:
        return False
