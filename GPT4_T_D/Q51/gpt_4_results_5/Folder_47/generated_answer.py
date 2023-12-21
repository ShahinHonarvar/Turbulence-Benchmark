
def if_contains_anagrams(lst):
    from itertools import combinations
    from collections import Counter
  
    total_anagrams = 0
    
    for first, second in combinations(lst, 2):
        first = first.lower()
        second = second.lower()
        
        if len(first) < 3 or len(second) < 3:
            continue
            
        if Counter(first) == Counter(second):
            total_anagrams += 1
            
            if total_anagrams > 366:
                return False
    return True
