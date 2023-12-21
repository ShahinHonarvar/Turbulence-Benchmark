
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters
    
    letters = [c.lower() for c in string if c.isalpha()]
    
    if len(letters) < 2:
        return set()
    
    perms = set(''.join(p) for p in permutations(letters, 2))
    
    palindromes = set()
    for p in perms:
        if p.lower() == p.lower()[::-1]:
            palindromes.add(p.lower())
    
    return palindromes
