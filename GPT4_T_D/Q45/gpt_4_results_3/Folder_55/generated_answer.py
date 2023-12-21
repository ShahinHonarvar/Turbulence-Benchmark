
from itertools import permutations

def palindromes_between_indices(str_arg):
    str_arg = str_arg[0:3]
    str_arg = str_arg.lower()
    
    palindromes = set()
    
    for i in range(3, len(str_arg) + 1):
        perms = permutations(str_arg, i)
        for perm in perms:
            perm_str = "".join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    
    return palindromes
