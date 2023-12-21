
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    arrangement = set(itertools.permutations(english_letters, r=5))
    palindromes = set()
    
    for chars in arrangement:
        palindrome = ''.join(chars) + ''.join(reversed(chars))
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
