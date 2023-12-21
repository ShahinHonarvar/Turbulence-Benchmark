
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    permutations = set(itertools.permutations(letters, 5))
    palindromes = set()
    
    for perm in permutations:
        word = "".join(perm)
        palindrome = word + word[::-1]
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome.lower())
    
    return palindromes
