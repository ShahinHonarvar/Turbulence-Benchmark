
def palindromes_between_indices(string):
    from itertools import permutations
    from string import ascii_letters
    
    letters = [c.lower() for c in string if c.isalpha()]
    if len(letters) < 3 or len(letters) < 5:
        return set()
    
    perms = set(''.join(p) for p in permutations(letters, 5))
    palindromes = set(p for p in perms if p.lower() == p.lower()[::-1])
    
    return palindromes
