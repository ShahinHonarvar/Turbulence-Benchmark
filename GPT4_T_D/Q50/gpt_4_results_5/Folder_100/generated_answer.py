
from collections import defaultdict 

def is_anagram(str1, str2): 
    return sorted(str1) == sorted(str2) 

def if_contains_anagrams(lst): 
    pairs = 0 
    for i in range(len(lst)): 
        if len(lst[i]) < 3: 
            continue 
        for j in range(i+1, len(lst)): 
            if len(lst[j]) < 3: 
                continue 
            if is_anagram(lst[i].lower(), lst[j].lower()): 
                pairs += 1 
                if pairs >= 95: 
                    return True 
    return False
