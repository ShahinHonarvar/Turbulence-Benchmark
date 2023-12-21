
import itertools

def palindromes_between_indices(str):
    substr = str[5:8].lower()
    substr_permutations = [''.join(perm) for perm in itertools.permutations(substr)]
    palindromes = set()
    for perm in substr_permutations:
        if len(perm) >= 4 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
