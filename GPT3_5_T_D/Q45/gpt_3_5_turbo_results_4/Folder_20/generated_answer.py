
import itertools

def palindromes_between_indices(string):
    string = string[2:9]
    letters = ''.join([char.lower() for char in string if char.isalpha()])
    all_palindromes = set()
    
    for combination in itertools.permutations(letters):
        palindrome = ''.join(combination)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            all_palindromes.add(palindrome)
    
    return all_palindromes
