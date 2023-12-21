
def palindromes_between_indices(string):
    import itertools
    
    letters = [ch for ch in string.lower() if ch.isalpha()]
    indices = range(5, 9)
    perms = set(itertools.permutations(letters, len(indices)))
    
    palindromes = set()
    
    for perm in perms:
        sub = ''.join(perm)
        if sub == sub[::-1] and len(sub) >= 3:
            palindromes.add(sub)
    
    return palindromes
