
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:6] if c.isalpha()]
    palindromes = set()
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
