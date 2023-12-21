
from itertools import permutations

def palindromes_between_indices(string):
    string = string[:9].lower()
    distinct_chars = list(set(string))
    palindromes = set()
    for len_palindrome in range(7, len(distinct_chars) + 1):
        for p in permutations(distinct_chars, len_palindrome):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
