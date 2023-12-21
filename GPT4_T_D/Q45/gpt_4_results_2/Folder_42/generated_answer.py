
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    all_pals = set()
    for i in range(3, len(s)+1):
        for comb in permutations(s, i):
            comb_string = ''.join(comb)
            if comb_string == comb_string[::-1]:
                all_pals.add(comb_string)
    return all_pals
