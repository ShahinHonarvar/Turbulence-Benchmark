
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    combinations = set(itertools.permutations(letters, 7))
    palindromes = set()
    
    for combination in combinations:
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
