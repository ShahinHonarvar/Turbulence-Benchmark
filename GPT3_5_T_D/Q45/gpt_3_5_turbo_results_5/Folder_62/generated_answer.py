
def palindromes_between_indices(s):
    import itertools
    from itertools import permutations
    
    letters = [char.lower() for char in s if char.isalpha()]
    
    if len(letters) < 7:
        return set()
    
    perms = [''.join(perm) for perm in permutations(letters, len(letters))]
    
    palindromes = set()
    for perm in perms:
        if perm[:9].lower() == perm[:9][::-1].lower():
            palindromes.add(perm[:9].lower())
    
    return palindromes
