
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string[4:9] if c.isalpha()]
    if len(letters) < 4:
        return set()

    letter_combinations = list(itertools.combinations(letters, 4))
    palindromes = set()
    for combination in letter_combinations:
        palindrome = ''.join(combination) + ''.join(combination[::-1])
        palindromes.add(palindrome.lower())
    
    return palindromes
