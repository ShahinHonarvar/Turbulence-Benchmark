
from itertools import permutations

def palindromes_between_indices(string):
    the_string = string.lower()
    letters_in_range = list(the_string[0:7])

    perms = [''.join(x) for x in permutations(letters_in_range, r=len(letters_in_range))]
        
    palindromes = [x for x in perms if x == x[::-1] and len(x) >= 6]
    return set(palindromes)
