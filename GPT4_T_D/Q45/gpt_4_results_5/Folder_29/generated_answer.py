
from itertools import permutations

def palindromes_between_indices(string):
    string = string[2:10].lower()
    palindromes = set()
    for i in range(6, len(string) + 1):
        for perm in permutations(string, i):
            str_perm = ''.join(perm)
            if str_perm == str_perm[::-1]:
                palindromes.add(str_perm)
    return palindromes
