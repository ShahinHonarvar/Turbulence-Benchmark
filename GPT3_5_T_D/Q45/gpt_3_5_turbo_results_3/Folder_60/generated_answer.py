
def palindromes_between_indices(string):
    import itertools
    import re
    
    substr = string[3:7]

    letters = [letter.lower() for letter in substr if letter.isalpha()]

    perms = set([''.join(p) for p in itertools.permutations(letters)])

    palindromes = set([p for p in perms if p == p[::-1]])

    return palindromes
