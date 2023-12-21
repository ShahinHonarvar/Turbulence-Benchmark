
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[6:10] if char.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation) + ''.join(permutation[::-1])
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
