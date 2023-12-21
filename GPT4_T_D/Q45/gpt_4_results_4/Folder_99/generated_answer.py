
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[4:9].lower()
    palindromes = set()
    for i in range(3, len(sub_string) + 1):
        perms = [''.join(p) for p in permutations(sub_string, i)]
        palindromes.update(set(filter(lambda x: x == x[::-1], perms)))
    return palindromes
