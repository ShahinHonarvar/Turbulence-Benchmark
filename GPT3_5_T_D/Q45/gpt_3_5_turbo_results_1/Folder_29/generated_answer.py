
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    combinations = itertools.permutations(letters, 8)
    palindromes = set()
    
    for combo in combinations:
        palindrome = ''.join(combo)
        if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 6:
            palindromes.add(palindrome)
    
    return palindromes
