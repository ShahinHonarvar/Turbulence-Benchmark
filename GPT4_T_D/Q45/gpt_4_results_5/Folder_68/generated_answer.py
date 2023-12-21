
from itertools import permutations

def palindromes_between_indices(strng):
    letters = strng[1:9].lower()
    palindromes = set()

    for i in range(4, len(letters) + 1):
        for perm in permutations(letters, i):
            possible_palindrome = ''.join(perm)
            if possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)

    return palindromes
