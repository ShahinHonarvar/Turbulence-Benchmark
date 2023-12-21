
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join([char for char in s if char in alphabets])

    result = set()
    for i in range(6, len(s)+1):
        for perm in permutations(s, i):
            possible_palindrome = ''.join(perm)
            if possible_palindrome == possible_palindrome[::-1]:
                result.add(possible_palindrome)
    return result
