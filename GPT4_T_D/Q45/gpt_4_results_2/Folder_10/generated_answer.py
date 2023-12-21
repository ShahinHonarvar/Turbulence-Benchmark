
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join(c for c in s if c in alphabet)
    palindromes = set()
    for i in range(3,len(s)+1):
        for subset in permutations(s,i):
            temp = ''.join(subset)
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes
