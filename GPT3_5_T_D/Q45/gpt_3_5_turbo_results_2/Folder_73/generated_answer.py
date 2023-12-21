
def palindromes_between_indices(string):
    import itertools
    import string
    
    letters = [letter.lower() for letter in string if letter.isalpha()]
    perm = list(itertools.permutations(letters, 4))
    palindromes = set()
    
    for p in perm:
        if p == p[::-1]:
            palindromes.add(''.join(p))
    
    return palindromes
