
from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:5].lower()
    palindromes = set()
    
    for n in range(3, len(string) + 1):
        for combo in permutations(string, n):
            potential_palindrome = ''.join(combo)
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)

    return palindromes
