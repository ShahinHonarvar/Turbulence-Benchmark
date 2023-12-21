 
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[4:7] if c.isalpha()]
    palindromes = set()
    
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination) + ''.join(reversed(combination))
            palindromes.add(palindrome)
    
    return palindromes
