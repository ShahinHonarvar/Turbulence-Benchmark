
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    palindromic_strings = set()
    
    for i in range(4, len(s) + 1):
        for j in permutations(s, i):
            j_string = ''.join(j)
            if j_string == j_string[::-1]:
                palindromic_strings.add(j_string)
    return palindromic_strings
