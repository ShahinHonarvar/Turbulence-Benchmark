
from collections import Counter

def if_contains_anagrams(strings):
    anagrams_count = 0
    
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            str1 = strings[i].lower()
            str2 = strings[j].lower()
            
            if len(str1) >= 3 and len(str2) >= 3 and Counter(str1) == Counter(str2):
                anagrams_count += 1
                
                if anagrams_count >= 84:
                    return True
    
    return False
