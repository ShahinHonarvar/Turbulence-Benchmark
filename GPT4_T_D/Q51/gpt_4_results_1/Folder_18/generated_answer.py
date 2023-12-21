
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
        
    anagrams = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and lst[i].lower() != lst[j].lower() and is_anagram(lst[i].lower(), lst[j].lower()):
                anagrams += 1
                if anagrams > 42:
                    return False
    return True
