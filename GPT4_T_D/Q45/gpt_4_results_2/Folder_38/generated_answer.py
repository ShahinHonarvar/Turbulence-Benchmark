
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join([char for char in s if char in alphabet])
    
    palindromes = set()
    for i in range(5, len(s) + 1):
        for perm in permutations(s, i):
            temp = ''.join(perm)
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes
