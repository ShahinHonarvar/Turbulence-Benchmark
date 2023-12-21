
from itertools import permutations 

def palindromes_between_indices(string):
    set_palindromes = set()
    string = string[1:9].lower()
    for i in range(7, len(string) + 1):
        perm = permutations(string, i)
        for i in list(perm):
            check_string = ''.join(i)
            if check_string == check_string[::-1]:
                set_palindromes.add(check_string)
    return set_palindromes
