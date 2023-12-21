
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10]
    s = s.lower()
    alphas = ''.join(ch for ch in s if ch.isalpha())
    unique_strings = set()
    
    for i in range(7, len(alphas) + 1):
        for permutation in permutations(alphas, i):
            current_string = ''.join(permutation)
            if current_string == current_string[::-1]:
                unique_strings.add(current_string)
                
    return unique_strings
