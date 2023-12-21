
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string if ch.isalpha()]
    if len(letters) < 7:
        return set()
    
    result = set()
    for perm in itertools.permutations(letters[:6]):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        if palindrome.lower() == palindrome:
            result.add(palindrome)
    
    return result
