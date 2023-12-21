
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[4:9]
    english_sub_string = "".join(char for char in sub_string if char.isalpha())
    english_sub_string = english_sub_string.lower()
    palindromes = set()

    for i in range(3,len(english_sub_string) +1):
        for perm in permutations(english_sub_string, i):
            possible_palindrome = "".join(perm)
            if possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)

    return palindromes
