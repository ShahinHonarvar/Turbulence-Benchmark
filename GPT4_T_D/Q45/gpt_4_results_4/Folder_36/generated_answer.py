
from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:9].lower()
    s = ''.join([i for i in s if i.isalpha()])
    palindromes = set()
    for i in range(3, len(s) + 1):
        for subset in permutations(s, i):
            potential_palindrome = ''.join(subset)
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes
