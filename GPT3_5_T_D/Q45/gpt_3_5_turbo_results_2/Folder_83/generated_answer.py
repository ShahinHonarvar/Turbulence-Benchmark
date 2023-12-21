
import itertools

def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter for letter in string[2:10].lower() if letter.isalpha()]
    num_letters = len(letters)
    
    if num_letters >= 7:
        for combination in itertools.permutations(letters, 7):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
