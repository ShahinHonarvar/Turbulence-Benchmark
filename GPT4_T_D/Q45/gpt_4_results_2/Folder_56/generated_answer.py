
from itertools import permutations

def palindromes_between_indices(string):
    string = string[5:10]
    palindromes = set()
    all_possible = [''.join(p) for p in permutations(string)]
    for i in all_possible:
        if len(i) >= 5 and i.lower() == i[::-1].lower():
            palindromes.add(i)
    return palindromes
