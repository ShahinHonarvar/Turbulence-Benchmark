
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                    anagrams += 1
                    if anagrams >= 50:
                        return True
    
    return False
