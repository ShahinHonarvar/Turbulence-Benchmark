
from collections import Counter

def if_contains_anagrams(lst):
    str_dicts = []

    for s in lst:
        if len(s) >= 3:
            counter = Counter(s.lower())
            str_dicts.append(counter)
            
    anagrams_count = 0
    
    for i in range(len(str_dicts)):
        for j in range(i+1, len(str_dicts)):
            if str_dicts[i] == str_dicts[j]:
                anagrams_count += 1

            if anagrams_count >= 61:
                return True
    
    return False
