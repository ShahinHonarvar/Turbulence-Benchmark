
from itertools import permutations

def palindromes_between_indices(s):
    sorted_sub_string = sorted(s[3:9].lower())
    palindromes = set()
    for i in range(5, len(sorted_sub_string)+1):
        for combination in permutations(sorted_sub_string, i):
            possible_palindrome = ''.join(combination)
            if possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)
    return palindromes
