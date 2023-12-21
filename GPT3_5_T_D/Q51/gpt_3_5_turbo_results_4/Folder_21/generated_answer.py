
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            
            if len(str1) >= 3 and len(str2) >= 3 and Counter(str1) == Counter(str2):
                count += 1
                
                if count > 26:
                    return False
    
    return True
