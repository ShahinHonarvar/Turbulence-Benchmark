
def palindromes_between_indices(string):
    from itertools import permutations
    
    letters = [ch for ch in string if ch.isalpha()]
    letters = [ch.lower() for ch in letters]
    
    perms = set(permutations(letters[:6], 6))
    palindromes = set()
    
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    
    return palindromes
