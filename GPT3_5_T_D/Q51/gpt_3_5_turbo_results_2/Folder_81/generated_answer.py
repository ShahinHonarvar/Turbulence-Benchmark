
import itertools

def if_contains_anagrams(lst):
    anagram_pairs = 0
    
    # Compare each pair of strings
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                # Convert strings to lowercase before comparison
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagram_pairs += 1
                    
            if anagram_pairs > 79:
                return False
    
    return True
