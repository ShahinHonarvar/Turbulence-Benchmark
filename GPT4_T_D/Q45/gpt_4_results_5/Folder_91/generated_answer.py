
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    palindromes = set()
    for s_length in range(3, len(s)+1):
        for subset in permutations(s, s_length):
            subset_string = ''.join(subset)
            if subset_string == subset_string[::-1]:
                palindromes.add(subset_string)
    return palindromes
