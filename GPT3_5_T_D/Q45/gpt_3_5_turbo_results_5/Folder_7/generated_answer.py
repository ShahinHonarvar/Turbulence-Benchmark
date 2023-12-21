
def palindromes_between_indices(string):
    import itertools
    
    letters = [ch.lower() for ch in string if ch.isalpha()]
    if len(letters) < 7:
        return set()
    
    perms = set(itertools.permutations(letters, 7))
    
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add("".join(perm))
    
    return palindromes
