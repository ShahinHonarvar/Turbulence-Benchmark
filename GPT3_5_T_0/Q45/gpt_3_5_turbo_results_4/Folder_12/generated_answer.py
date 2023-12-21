
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for length in range(4, 9):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
