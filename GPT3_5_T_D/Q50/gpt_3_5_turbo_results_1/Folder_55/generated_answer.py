
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    
    for i in range(len(lst)):
        counter_1 = Counter(lst[i].lower())
        
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if counter_1 == Counter(lst[j].lower()):
                    count += 1
                    
                    if count >= 15:
                        return True
    
    return False
