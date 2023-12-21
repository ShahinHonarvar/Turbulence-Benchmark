
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()                       
    palindromes_set = set()
    for i in range(3,len(s)+1):              
        perms = set(permutations(s, i))          
        for perm in perms:              
            word = ''.join(perm)                
            if word == word[::-1]:             
                palindromes_set.add(word)
    return palindromes_set
