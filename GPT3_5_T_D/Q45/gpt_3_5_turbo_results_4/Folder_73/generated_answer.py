
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    arrangement = letters[3:7]
    palindromes = set()
    
    for perm in itertools.permutations(arrangement):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)

    return palindromes if len(palindromes) > 0 else set()
