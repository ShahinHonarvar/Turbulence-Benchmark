
from itertools import permutations 

def palindromes_between_indices(string): 
  
    palindromes = set() 
  
    substring = string[1:9]

    perms = [''.join(p) for p in permutations(substring) if len(p) >= 4] 
    
    for perm in perms: 
      
        if perm.lower() == perm[::-1].lower():
            palindromes.add(perm) 
  
    return palindromes
