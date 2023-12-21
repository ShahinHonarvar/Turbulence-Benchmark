
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [char for char in string[:9] if char.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(combination)
        if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
