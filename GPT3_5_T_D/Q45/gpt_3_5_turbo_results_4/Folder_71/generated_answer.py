
def palindromes_between_indices(string):
    import itertools
    
    letters = [c.lower() for c in string[1:4] if c.isalpha()]
    
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
