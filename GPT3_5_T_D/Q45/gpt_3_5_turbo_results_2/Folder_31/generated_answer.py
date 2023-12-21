
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:9] if c.isalpha()] # extract English letters from index 1 to 8
    perms = itertools.permutations(letters) # get all possible arrangements
    palindromes = set()
    
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6: # check if the word is a palindrome of length at least 6
            palindromes.add(word)
    
    return palindromes
