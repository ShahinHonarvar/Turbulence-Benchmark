
import itertools

def palindromes_between_indices(string: str) -> set:
    letters = [char.lower() for char in string[2:8] if char.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
    
    return palindromes
