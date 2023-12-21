
from itertools import permutations

def palindromes_between_indices(string):
    string = string[3:6]
    palindromes = set()
    for permutation in permutations(string):
        temp = "".join(permutation).lower()
        if temp == temp[::-1] and len(temp) >= 4:
            palindromes.add(temp)
    return palindromes
