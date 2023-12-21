
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[2:5] if c.isalpha()]
    possible_combinations = itertools.permutations(letters)
    palindromes = set()
    
    for combination in possible_combinations:
        palindrome = ''.join(combination) + ''.join(reversed(combination))
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
