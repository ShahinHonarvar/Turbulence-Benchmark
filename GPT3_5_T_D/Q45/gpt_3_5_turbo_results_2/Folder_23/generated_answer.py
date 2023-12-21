
def palindromes_between_indices(string):
    import itertools
    
    letters = [c.lower() for c in string if c.isalpha()]
    letters = letters[:7]
    permutations = set(itertools.permutations(letters, 4))
    
    palindromes = set()
    
    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
