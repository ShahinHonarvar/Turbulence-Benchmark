
from collections import Counter 

def if_contains_anagrams(list_of_strings):
    c = Counter()
    
    for string in list_of_strings:
        if len(string) >= 3:
            c["".join(sorted(string.lower()))] += 1
            
    pairs = sum(v*(v-1)//2 for v in c.values())
    
    return pairs >= 89
