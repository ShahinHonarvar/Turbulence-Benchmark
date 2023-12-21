 
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    
    for length in range(4, 7):
        for combo in itertools.permutations(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.casefold())
    
    return palindromes
