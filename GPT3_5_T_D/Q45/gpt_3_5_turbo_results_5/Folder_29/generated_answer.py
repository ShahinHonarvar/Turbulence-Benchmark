
import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string[2:10].lower() if letter.isalpha()]
    all_palindromes = set()
    
    for perm in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            all_palindromes.add(palindrome)
            
    return all_palindromes
