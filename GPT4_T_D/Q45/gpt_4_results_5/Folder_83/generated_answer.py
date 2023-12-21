
from itertools import permutations

def palindromes_between_indices(string):
    string = string[2: 10]
    all_pals = set()
    for i in range(7, len(string)+1):
        for subset in permutations(string, i):
            subset = ''.join(subset).lower()
            if subset == subset[::-1]:
                all_pals.add(subset)
    return all_pals
