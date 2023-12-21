
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string if ch.isalpha()]
    combinations = set(itertools.combinations(letters, 8))
    palindromes = set()
    
    for comb in combinations:
        palindrome = ''.join(comb)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
