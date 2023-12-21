
from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    anagram_count = 0
    
    for string in strings:
        if len(string) < 3:
            continue
            
        lower_string = string.lower()
        string_counter = Counter(lower_string)
        key = ''.join(sorted(lower_string))
        
        if string_counter == counter[key]:
            anagram_count += 1
            
        counter[key] = string_counter
        
        if anagram_count > 34:
            return False
    
    return True
