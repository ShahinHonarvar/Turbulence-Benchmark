
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for combo in permutations(s, i):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
