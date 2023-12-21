
import itertools

def if_contains_anagrams(strings):
    count = 0
    
    # Helper function to check if two strings are anagrams
    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    # Generate all possible pairs of strings
    pairs = itertools.combinations(strings, 2)
    
    for pair in pairs:
        if are_anagrams(pair[0], pair[1]) and len(pair[0]) >= 3:
            count += 1
            
            # If the count exceeds 74, return False
            if count > 74:
                return False
    
    return True
