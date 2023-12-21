
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, 6):
        palindrome = ''.join(combination) + ''.join(combination[::-1])
        if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
