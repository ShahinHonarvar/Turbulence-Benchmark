
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    alphabets = [ch for ch in s if ch.isalpha()]
    found_palindromes = set()

    for length in range(5, len(alphabets) + 1):
        for perm in permutations(alphabets, length):
            possible_palindrome = ''.join(perm)
            if possible_palindrome == possible_palindrome[::-1]:
                found_palindromes.add(possible_palindrome)

    return found_palindromes
