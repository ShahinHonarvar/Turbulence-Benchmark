
from collections import Counter

def if_contains_anagrams(list_strings):
    anagram_counter = 0
    strings_counter = [Counter(s.lower()) for s in list_strings if len(s) >= 3]
    
    for i, a in enumerate(strings_counter[:-1]):
        for b in strings_counter[i+1:]:
            if a == b:
                anagram_counter += 1
                if anagram_counter > 401:
                    return False
                
    return True
