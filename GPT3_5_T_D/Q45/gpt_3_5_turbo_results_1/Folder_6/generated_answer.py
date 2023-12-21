
import itertools

def palindromes_between_indices(string):
    letters = ''.join([c.lower() for c in string if c.isalpha()])
    substrings = set()
    
    for length in range(4, 8):
        for permutation in itertools.permutations(letters, length):
            palindrome = ''.join(permutation)
            if palindrome == palindrome[::-1]:
                substrings.add(palindrome)
    
    return substrings
