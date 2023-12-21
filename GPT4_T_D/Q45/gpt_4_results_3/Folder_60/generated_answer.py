
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    possible_palindromes = set()
    for i in range(4, len(s) + 1):
        for perm in permutations(s, i):
            perm_string = ''.join(perm)
            if perm_string == perm_string[::-1]:
                possible_palindromes.add(perm_string)
    return possible_palindromes
