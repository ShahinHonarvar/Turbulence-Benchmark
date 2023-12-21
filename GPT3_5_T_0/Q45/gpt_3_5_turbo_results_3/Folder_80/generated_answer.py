
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.combinations(letters, 6):
        for permutation in itertools.permutations(combination):
            palindrome = ''.join(permutation)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
