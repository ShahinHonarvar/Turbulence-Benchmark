
from itertools import permutations

def palindromes_between_indices(string):
    string = string[3:8].lower()
    result = set()
    for i in range(4, len(string) + 1):
        for comb in permutations(string, i):
            possible_palindrome = ''.join(comb)
            if possible_palindrome == possible_palindrome[::-1]:
                result.add(possible_palindrome)
    return result
