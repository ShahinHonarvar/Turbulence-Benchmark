
import itertools

def palindromes_between_indices(s):
    pali_set = set()
    s = s[1:8].lower()
    
    for pali_len in range(7, len(s)+1):
        combinations = itertools.permutations(s, pali_len)
        
        for combo in combinations:
            combo_str = ''.join(combo)
            
            if combo_str == combo_str[::-1]:
                pali_set.add(combo_str)
    
    return pali_set
