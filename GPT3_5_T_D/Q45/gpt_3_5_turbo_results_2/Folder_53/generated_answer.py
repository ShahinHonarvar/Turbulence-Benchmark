
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[4:9] if ch.isalpha()]
    if len(letters) < 6:
        return set()

    palindromes = set()
    for combination in itertools.permutations(letters, 6):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
