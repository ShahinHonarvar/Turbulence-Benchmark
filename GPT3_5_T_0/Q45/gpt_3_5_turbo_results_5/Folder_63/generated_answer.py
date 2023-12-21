
def palindromes_between_indices(string):
    import itertools
    import string
    
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters, 4):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
