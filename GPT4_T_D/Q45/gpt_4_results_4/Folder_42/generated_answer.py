
from itertools import permutations

def palindromes_between_indices(string):
    slice_str = string[6:10].lower()
    palindromes = set()

    for i in range(3, len(slice_str)+1):
        for perm in permutations(slice_str, i):
            current_perm = ''.join(perm)
            if current_perm == current_perm[::-1]:
                palindromes.add(current_perm)
                
    return palindromes
