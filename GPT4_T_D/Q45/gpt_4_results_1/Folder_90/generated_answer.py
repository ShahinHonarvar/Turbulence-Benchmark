
from itertools import permutations

def palindromes_between_indices(string):
    string = string[:6].lower()
    palindromes = set()
    for length in range(4, len(string) + 1):
        for perm in permutations(string, length):
            palindrome_candidate = "".join(perm)
            if palindrome_candidate == palindrome_candidate[::-1]:
                palindromes.add(palindrome_candidate)
    return palindromes
