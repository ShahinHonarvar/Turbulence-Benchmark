
from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:10].lower()
    palindromes = set()
    for perm in permutations(s):
        temp = ''.join(perm)
        if temp == temp[::-1] and len(temp) >= 4:
            palindromes.add(temp)
    return palindromes
