
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            str_perm = ''.join(perm)
            if str_perm == str_perm[::-1]:
                palindromes.add(str_perm)
    return palindromes
