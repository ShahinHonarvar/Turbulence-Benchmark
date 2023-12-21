
from itertools import permutations

def palindromes_between_indices(s):
    str_subset = s[5:8]
    character_set = set()
    for i in range(4, len(str_subset) + 1):
        for item in permutations(str_subset, i):
            possible_palindrome = ''.join(item)
            if possible_palindrome.lower() == possible_palindrome.lower()[::-1]:
                character_set.add(possible_palindrome.lower())

    return character_set
